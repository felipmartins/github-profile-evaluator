import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from time import sleep
from .utils import csv_to_list
from django.shortcuts import render, redirect, get_object_or_404
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
from evaluator.fetch import single_fetch_content
from evaluator.data_getter import populate_dict
from evaluator.evaluation import single_evaluation, do_group_evaluation
from evaluator.create_evaluation import new_evaluation, new_group_evaluation
from evaluator.models import Evaluation, GroupCSV, GroupEvaluation
from evaluator.tracker import raise_evaluation_clicks


def index(request):
    context = {}
    if request.method == "POST":
        print(request.POST["github_user"])
        eval = single_evaluation(
            populate_dict(single_fetch_content(request.POST["github_user"]))
        )
        new_eval = new_evaluation(eval)
        raise_evaluation_clicks()
        return redirect("evaluation", uuid=new_eval.uuid)

    return render(request, "index.html", context)


def group_index(request):
    context = {}

    if request.method == "POST":
        if request.FILES["file"]._name.endswith("csv"):
            csv_object = GroupCSV(file=request.FILES["file"])
            csv_object.save()
            csv_list = csv_to_list(csv_object.file.name)
            if "github_username" not in csv_list[0]:
                csv_object.file.delete()
                csv_object.delete()
                request.session[
                    "erro"
                ] = 'Chave "github_username" não existe no arquivo!!'
                return redirect("group-homepage")
            if "erro" in request.session:
                del request.session["erro"]
            csv_list = do_group_evaluation(csv_list)
            new_group_evaluation(csv_list, csv_object)
            raise_evaluation_clicks
            sleep(1)
            return redirect("group-evaluation", uuid=csv_object.uuid)
        else:
            request.session["erro"] = "Arquivo Inválido!!"
            return redirect("group-homepage")

    return render(request, "group_index.html", context)


def evaluation(request, uuid: str):
    current_evaluation = get_object_or_404(Evaluation, uuid=uuid)
    context = {"evaluation": current_evaluation, "single": "single"}
    return render(request, "evaluation.html", context)


def group_evaluation(request, uuid: str):
    csv_object = get_object_or_404(GroupCSV, uuid=uuid)
    evaluations = GroupEvaluation.objects.all().filter(csv_file=csv_object)

    context = {"group_evaluation": evaluations, "group": "group"}
    return render(request, "group_evaluation.html", context)


def pdf_export(request, type: str, uuid: str):
    if type == "group":
        csv_object = get_object_or_404(GroupCSV, uuid=uuid)
        evaluations = GroupEvaluation.objects.all().filter(csv_file=csv_object)
    else:
        current_evaluation = get_object_or_404(Evaluation, uuid=uuid)
        evaluations = [current_evaluation]

    height = 0

    print(evaluations)

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)  # *2,83 ~(595, 842)

    for evaluation in evaluations:

        p.setFont("Helvetica-Bold", 30)
        height += 45
        p.drawCentredString(
            A4[0] / 2.0,
            A4[1] - height,
            "Avaliação realizada em " + evaluation.evaluation_date.strftime("%d/%m/%Y"),
        )
        logo = ImageReader(
            "evaluator/static/photos/" + evaluation.github_user + "_image.jpg"
        )
        logo.getSize()
        width = logo._width
        height += 235
        p.drawImage(
            logo,
            A4[0] / 2 - width / 2,
            A4[1] - height,
            height=200,
            preserveAspectRatio=True,
            mask=None,
        )
        p.setFont("Helvetica-Bold", 25)
        height += 45
        p.drawCentredString(A4[0] / 2, A4[1] - height, str(evaluation))
        data = [["Critérios de Avaliação", "Encontrado", "Esperado", "Avaliação"]]
        if evaluation.has_photo:
            pergunta1 = [
                "Rosto encontrado pelo algoritmo na foto de perfil?",
                "Sim!",
                "Sim!",
                "+10 pontos",
            ]
        else:
            pergunta1 = [
                "Rosto encontrado pelo algoritmo na foto de perfil?",
                "Não",
                "Sim!",
                "0 pontos",
            ]
        if evaluation.has_email:
            pergunta2 = [
                "E-mail localizado dentro do README?",
                "Sim!",
                "Sim!",
                "+10 pontos",
            ]
        else:
            pergunta2 = [
                "E-mail localizado dentro do README?",
                "Não",
                "Sim!",
                "0 pontos",
            ]
        if evaluation.has_linkedin:
            pergunta3 = [
                "LinkedIn localizado dentro do GitHub?",
                "Sim!",
                "Sim!",
                "+10 pontos",
            ]
        else:
            pergunta3 = [
                "LinkedIn localizado dentro do GitHub?",
                "Não",
                "Sim!",
                "0 pontos",
            ]
        if evaluation.stacks >= 5:
            pergunta4 = [
                "Tecnologias de domínio localizadas no perfil",
                evaluation.stacks,
                ">=5",
                "+10 pontos",
            ]
        else:
            pergunta4 = [
                "Tecnologias de domínio localizadas no perfil",
                evaluation.stacks,
                ">=5",
                "0 pontos",
            ]
        if evaluation.stacks >= 10:
            pergunta5 = [
                "Tecnologias de domínio localizadas no perfil",
                evaluation.stacks,
                ">=10",
                "+10 pontos",
            ]
        else:
            pergunta5 = [
                "Tecnologias de domínio localizadas no perfil",
                evaluation.stacks,
                ">=10",
                "0 pontos",
            ]
        if evaluation.repositories >= 5:
            pergunta6 = [
                "Repositórios públicos localizados no GitHub",
                evaluation.repositories,
                ">=5",
                "+10 pontos",
            ]
        else:
            pergunta6 = [
                "Repositórios públicos localizados no GitHub",
                evaluation.repositories,
                ">=5",
                "0 pontos",
            ]
        if evaluation.repositories >= 10:
            pergunta7 = [
                "Repositórios públicos localizados no GitHub",
                evaluation.repositories,
                ">=10",
                "+10 pontos",
            ]
        else:
            pergunta7 = [
                "Repositórios públicos localizados no GitHub",
                evaluation.repositories,
                ">=10",
                "0 pontos",
            ]
        if evaluation.pinned_repositories >= 2:
            pergunta8 = [
                "Repositórios pinados localizados no GitHub",
                evaluation.pinned_repositories,
                ">=5",
                "+10 pontos",
            ]
        else:
            pergunta8 = [
                "Repositórios pinados localizados no GitHub",
                evaluation.pinned_repositories,
                ">=5",
                "0 pontos",
            ]
        if evaluation.pinned_repositories >= 4:
            pergunta9 = [
                "Repositórios pinados localizados no GitHub",
                evaluation.pinned_repositories,
                ">=10",
                "+10 pontos",
            ]
        else:
            pergunta9 = [
                "Repositórios pinados localizados no GitHub",
                evaluation.pinned_repositories,
                ">=10",
                "0 pontos",
            ]

        data.append(pergunta1)
        data.append(pergunta2)
        data.append(pergunta3)
        data.append(pergunta4)
        data.append(pergunta5)
        data.append(pergunta6)
        data.append(pergunta7)
        data.append(pergunta8)
        data.append(pergunta9)

        f = Table(
            data,
            colWidths=[270, 90, 90, 90],
            rowHeights=[25, 25, 25, 25, 25, 25, 25, 25, 25, 25],
        )
        f.setStyle(
            TableStyle(
                [
                    ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
                    ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                    ("ALIGN", (1, 0), (-1, -1), "CENTER"),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.Color(red=(0.1), green=(0.1), blue=(0.1)),
                    ),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 15),
                    ("FONTNAME", (0, 1), (-1, -1), "Helvetica-Bold"),
                ]
            )
        )

        height += 275

        f.wrapOn(p, 475, 250)
        f.drawOn(p, A4[0] / 2 - 270, A4[1] - height)

        p.showPage()
        height = 0

    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
