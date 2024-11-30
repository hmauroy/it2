"""
Funksjoner som beskriver hva en minibank kan gjøre.
"""


def sjekk_saldo(kontonr, kontoer):
    if kontonr in kontoer:
        return kontoer[kontonr]['saldo']
    return "Konto ikke funnet"


def innskudd(kontonr, belop, kontoer):
    if kontonr in kontoer:
        kontoer[kontonr]['saldo'] += belop
        kontoer[kontonr]['transaksjoner'].append(f"Innskudd: +{belop} kr")
        return kontoer[kontonr]['saldo']
    return "Konto ikke funnet"


def uttak(kontonr, belop, kontoer):
    if kontonr in kontoer:
        if kontoer[kontonr]['saldo'] >= belop:
            kontoer[kontonr]['saldo'] += belop
            kontoer[kontonr]['transaksjoner'].append(f"Uttak: -{belop} kr")
            return kontoer[kontonr]['saldo']
        return "Ikke nok saldo"
    return "Konto ikke funnet"


def overføring(fra_kontonr, til_kontonr, belop, kontoer):
    if fra_kontonr in kontoer and til_kontonr in kontoer:
        if kontoer[fra_kontonr]['saldo'] >= belop:
            kontoer[fra_kontonr]['saldo'] -= belop
            kontoer[fra_kontonr]['transaksjoner'].append(
                f"Overføring til {til_kontonr}: -{belop} kr")
            kontoer[til_kontonr]['saldo'] += belop
            kontoer[til_kontonr]['transaksjoner'].append(
                f"Overføring fra {fra_kontonr}: +{belop} kr")
            return kontoer[fra_kontonr]['saldo'], kontoer[til_kontonr]['saldo']
        return "Ikke nok saldo på avsenderkonto"
    return "En eller begge kontoer ble ikke funnet"


def vis_transaksjonshistorikk(kontonr, kontoer):
    if kontonr in kontoer:
        return kontoer[kontonr]['transaksjoner']
    return "Konto ikke funnet"
