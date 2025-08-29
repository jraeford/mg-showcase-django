
from django.core.management.base import BaseCommand
from members.models import Member, Media, Social

class Command(BaseCommand):
    help = "Seed demo data"

    def handle(self, *args, **options):
        Member.objects.all().delete()
        alex = Member.objects.create(
            slug="alex",
            name="Alex Johnson",
            title="Data Analyst",
            summary="Early-career data analyst using AI for good.",
            location="Durham, NC",
            skills="Python, Pandas, Prompt Engineering",
            goals="Build nonprofit dashboard; Master agentic AI",
            email="alex@example.com",
        )
        Social.objects.create(member=alex, platform="LinkedIn", url="https://linkedin.com")
        Media.objects.create(member=alex, type=Media.IMAGE, url="https://placehold.co/800x450", caption="Demo Image")

        self.stdout.write(self.style.SUCCESS("Seeded demo data."))
