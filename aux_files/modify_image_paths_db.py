from django.core.management.base import BaseCommand
from movie.models import Movie
import json
import os
import openai
import requests
from PIL import Image
from io import BytesIO

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv('../openAI.env')
openai.api_key  = os.environ['openAI_api_key']

def fetch_image(url):
    response = requests.get(url)
    response.raise_for_status()

    # Convert the response content into a PIL Image
    image = Image.open(BytesIO(response.content))
    return(image)

class Command(BaseCommand):
    help = 'Modify path of images'

    def handle(self, *args, **kwargs):
        items = Movie.objects.all()
        for item in items:
            item.image.name = f"{item.image.name[0:13]}{item.title}.jpg" 
            item.save()
        
        #self.stdout.write(self.style.SUCCESS(f'Successfully updated item with ID {item_id}'))
        