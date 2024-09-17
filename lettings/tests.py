import pytest
from django.urls import reverse
from lettings.models import Address, Letting
from django.test import Client


client = Client()


@pytest.mark.django_db
class TestLettings:
    def test_address_model(self):
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TST",
        )
        assert str(address) == "123 Test Street"

    def test_letting_model(self):
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TST",
        )
        letting = Letting.objects.create(title="Test Letting", address=address)
        assert str(letting) == "Test Letting"

    def test_lettings_index_view(self, client):
        url = reverse("lettings:index")
        response = client.get(url)
        assert response.status_code == 200
        assert "lettings/index.html" in [t.name for t in response.templates]

    def test_letting_detail_view(self, client):
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TST",
        )
        letting = Letting.objects.create(title="Test Letting", address=address)
        url = reverse("lettings:letting", args=[letting.id])
        response = client.get(url)
        assert response.status_code == 200
        assert "lettings/letting.html" in [t.name for t in response.templates]
        assert "Test Letting" in str(response.content)
