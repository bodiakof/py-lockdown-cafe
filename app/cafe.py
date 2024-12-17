import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor does not have a vaccine record.")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine has expired.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"