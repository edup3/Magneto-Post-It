import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import requests
from PIL import Image
from io import BytesIO
import numpy as np
from image_generator.models import Vacante, Usuario
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
    return image

def generar_imagen(vacante:Vacante):
        custom_user = Usuario.objects.get(user = vacante.empleador.id)
        response = client.images.generate(
            model="dall-e-3",
            prompt=f"Imagen que respresente el trabajo de {vacante.nombre_vacante},   la imagen tiene que cumplir con la descripcion {vacante.descripcion}, y en lo posible usar los siguientes colores que estan en formato hexadecimal: {custom_user.colors}",
            size="1024x1024",
            quality="standard",
            n=1,
            )
        image_url = response.data[0].url
        image = fetch_image(image_url)
        return image
        
def guardar_imagen(vacante:Vacante, imagen:Image):
    imagen.save(f'{MEDIA_ROOT}/images/{vacante.nombre_vacante}_id_{vacante.id}.jpg')
    vacante.imagen = f'images/{vacante.nombre_vacante}_id_{vacante.id}.jpg'
    vacante.save()