studenci_dict=[
     {
        "imie": "Mateusz",
        "nazwisko": "Karcza",
        "wiek": 21,
        "adres email": "kar.mateusz@wp.pl",
        "rok uroczenia": "1997",
        "adres": "surowe 157"
    },{
        "imie": "Bartosz",
        "nazwisko": "H.",
        "wiek": 21,
        "adres email": "h.barosz@gmail.com",
        "rok uroczenia": "1997",
        "adres": "czrna dziura"
    },
    {
        "imie": "Tomasz",
        "nazwisko": "K.",
        "wiek": 21,
        "adres email": "k.tomasz@gmai.com",
        "rok uroczenia": "1997",
        "adres": "nidzica"
    }
]
for i in studenci_dict:
    print("{} {} lat {:d} urodzony {} zamieszkały {} email {}".format(
        i["imie"],i["nazwisko"],i["wiek"],i["rok uroczenia"],i["adres"],i["adres email"]))