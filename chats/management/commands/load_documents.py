
from django.core.management.base import BaseCommand
from chats.models import DocumentChunk
from chats.rag import get_embedding

class Command(BaseCommand):
    help = "Load academic documents into vector database"

    def handle(self, *args, **kwargs):
        documents = [
            "Course registration must be completed within the first two weeks of semester.",
            "Students must submit academic transcripts during registration.",
            "Late registration requires approval from academic office."
        ]

        for text in documents:
            embedding = get_embedding(text)
            DocumentChunk.objects.create(
                content=text,
                embedding=embedding
            )

        self.stdout.write(self.style.SUCCESS("Documents loaded successfully."))