import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import requests
from PIL import Image
from io import BytesIO
import numpy as np
from image_generator.models import Vacante
from magnetopostit.settings import MEDIA_ROOT

_ = load_dotenv('openAI.env')
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get('openAI_api_key'),
)


def fetch_image(url):
    response = requests.get(url)
    response.raise_for_status()

    # Convert the response content into a PIL Image
    image = Image.open(BytesIO(response.content))
    return(image)

def generar_imagen(vacante:Vacante):
        response = client.images.generate(
            model="dall-e-3",
            prompt=f"Imagen que respresente el trabajo de {vacante.nombre_vacante},   la imagen tiene que cumplir con la descripcion {vacante.descripcion}",
            size="1024x1024",
            quality="standard",
            n=1,
            )
        image_url = response.data[0].url
        image = fetch_image(image_url)
        image.save(f'{MEDIA_ROOT}/images/{vacante.nombre_vacante}_id_{vacante.id}.jpg')
        vacante.imagen = f'images/{vacante.nombre_vacante}_id_{vacante.id}.jpg'
        vacante.save()