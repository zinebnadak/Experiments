Skapa ett program som fungerar som en enkel telefonkatalog.

Varje person i katalogen ska kunna ha flera telefonnummer, och varje nummer ska vara kopplat till en viss kategori (“mobil”, “hem”, “jobb”, etc). För att möjliggöra detta kan du använda nästlade dictionaries: ett dictionary som innehåller andra dictionaries.

Exempel:

directory = {
    "Anna": {
        "mobil": "+358457123456",
        "hem": "0185551111"
    },
    "Bertil": {
        "jobb": "04001998877"
    }
}

directory["Anna"]["hem"] motsvarar alltså Annas mobilnummer 0185551111.

Ditt program ska åtminstone kunna hantera följande:
Personer
Lägg till en person i katalogen.
Ta bort en person från katalogen.
Visa alla personer (endast namn) i katalogen.
Sök efter en person och visa dennes telefonnummer.
Telefonnummer
Lägg till ett nummer för en viss person.
Ta bort ett nummer för en viss person.
Uppdatera ett nummer för en viss person.


Hur programmet ska presenteras för användaren är upp till dig. Du kan använda en enda meny med många alternativ, eller använda dig av flera menynivåer.

Sträva efter användarvänlighet och datasäkerhet: Fråga till exempel användaren om hen verkligen vill ta bort eller ersätta befintlig information.

För denna uppgift finns ingen given funktionsindelning, men programmet bör vara uppdelat i lämpliga funktioner och moduler.

För den intresserade finns många frivilliga utvidgningsmöjligheter, t.ex:
- möjlighet att spara flera nummer under samma kategori
- möjlighet att också spara adress och andra kontaktuppgifter
- möjlighet att spara information permanent till fil, i JSON-format (se kapitel 12.3 i kursboken)


"""Create a Simple Phone Directory Program

Each person can have multiple phone numbers, each linked to a category (e.g., "mobile", "home", "work").
Use nested dictionaries: a dictionary containing other dictionaries.

Program should at least handle:

People:
- Add a person
- Remove a person
- Show all people (names only)
- Search for a person and display their numbers

Phone numbers:
- Add a number for a person
- Remove a number for a person
- Update a number for a person

User interface:
- Can be a single menu or multiple levels
- Should be user-friendly and safe (ask for confirmation before deleting or replacing data)

Program structure:
- No strict function requirements, but should be organized into suitable functions/modules

Optional extensions:
- Allow multiple numbers under the same category
- Store addresses and other contact info
- Save data permanently to a file (JSON format)
"""
