# Conjugaisons de base pour certains verbes à titre d'exemple
import random
from rich.console import Console

console = Console()


# Dictionnaire complet des conjugaisons pour chaque verbe et temps
conjugaisons = {
    'aimer': {
        'présent': ['j\' aime', 'tu aimes', 'il/elle/on aime', 'nous aimons', 'vous aimez', 'ils/elles aiment'],
        'passé composé': ['j\' ai aimé', 'tu as aimé', 'il/elle/on a aimé', 'nous avons aimé', 'vous avez aimé', 'ils/elles ont aimé'],
        'imparfait': ['j\' aimais', 'tu aimais', 'il/elle/on aimait', 'nous aimions', 'vous aimiez', 'ils/elles aimaient'],
        'futur simple': ['j\' aimerai', 'tu aimeras', 'il/elle/on aimera', 'nous aimerons', 'vous aimerez', 'ils/elles aimeront'],
        'conditionnel présent': ['j\' aimerais', 'tu aimerais', 'il/elle/on aimerait', 'nous aimerions', 'vous aimeriez', 'ils/elles aimeraient'],
        'passé simple': ['j\' aimai', 'tu aimas', 'il/elle/on aima', 'nous aimâmes', 'vous aimâtes', 'ils/elles aimèrent']
    },
    'parler': {
        'présent': ['je parle', 'tu parles', 'il/elle/on parle', 'nous parlons', 'vous parlez', 'ils/elles parlent'],
        'passé composé': ['j\' ai parlé', 'tu as parlé', 'il/elle/on a parlé', 'nous avons parlé', 'vous avez parlé', 'ils/elles ont parlé'],
        'imparfait': ['je parlais', 'tu parlais', 'il/elle/on parlait', 'nous parlions', 'vous parliez', 'ils/elles parlaient'],
        'futur simple': ['je parlerai', 'tu parleras', 'il/elle/on parlera', 'nous parlerons', 'vous parlerez', 'ils/elles parleront'],
        'conditionnel présent': ['je parlerais', 'tu parlerais', 'il/elle/on parlerait', 'nous parlerions', 'vous parleriez', 'ils/elles parleraient'],
        'passé simple': ['je parlai', 'tu parlas', 'il/elle/on parla', 'nous parlâmes', 'vous parlâtes', 'ils/elles parlèrent']
    },
    'donner': {
        'présent': ['je donne', 'tu donnes', 'il/elle/on donne', 'nous donnons', 'vous donnez', 'ils/elles donnent'],
        'passé composé': ['j\' ai donné', 'tu as donné', 'il/elle/on a donné', 'nous avons donné', 'vous avez donné', 'ils/elles ont donné'],
        'imparfait': ['je donnais', 'tu donnais', 'il/elle/on donnait', 'nous donnions', 'vous donniez', 'ils/elles donnaient'],
        'futur simple': ['je donnerai', 'tu donneras', 'il/elle/on donnera', 'nous donnerons', 'vous donnerez', 'ils/elles donneront'],
        'conditionnel présent': ['je donnerais', 'tu donnerais', 'il/elle/on donnerait', 'nous donnerions', 'vous donneriez', 'ils/elles donneraient'],
        'passé simple': ['je donnai', 'tu donnas', 'il/elle/on donna', 'nous donnâmes', 'vous donnâtes', 'ils/elles donnèrent']
    },
    'chanter': {
        'présent': ['je chante', 'tu chantes', 'il/elle/on chante', 'nous chantons', 'vous chantez', 'ils/elles chantent'],
        'passé composé': ['j\' ai chanté', 'tu as chanté', 'il/elle/on a chanté', 'nous avons chanté', 'vous avez chanté', 'ils/elles ont chanté'],
        'imparfait': ['je chantais', 'tu chantais', 'il/elle/on chantait', 'nous chantions', 'vous chantiez', 'ils/elles chantaient'],
        'futur simple': ['je chanterai', 'tu chanteras', 'il/elle/on chantera', 'nous chanterons', 'vous chanterez', 'ils/elles chanteront'],
        'conditionnel présent': ['je chanterais', 'tu chanterais', 'il/elle/on chanterait', 'nous chanterions', 'vous chanteriez', 'ils/elles chanteraient'],
        'passé simple': ['je chantai', 'tu chantas', 'il/elle/on chanta', 'nous chantâmes', 'vous chantâtes', 'ils/elles chantèrent']
    },
    'jouer': {
        'présent': ['je joue', 'tu joues', 'il/elle/on joue', 'nous jouons', 'vous jouez', 'ils/elles jouent'],
        'passé composé': ['j\' ai joué', 'tu as joué', 'il/elle/on a joué', 'nous avons joué', 'vous avez joué', 'ils/elles ont joué'],
        'imparfait': ['je jouais', 'tu jouais', 'il/elle/on jouait', 'nous jouions', 'vous jouiez', 'ils/elles jouaient'],
        'futur simple': ['je jouerai', 'tu joueras', 'il/elle/on jouera', 'nous jouerons', 'vous jouerez', 'ils/elles joueront'],
        'conditionnel présent': ['je jouerais', 'tu jouerais', 'il/elle/on jouerait', 'nous jouerions', 'vous joueriez', 'ils/elles joueraient'],
        'passé simple': ['je jouai', 'tu jouas', 'il/elle/on joua', 'nous jouâmes', 'vous jouâtes', 'ils/elles jouèrent']
    },

    # Verbes du deuxième groupe
    'finir': {
        'présent': ['je finis', 'tu finis', 'il/elle/on finit', 'nous finissons', 'vous finissez', 'ils/elles finissent'],
        'passé composé': ['j\' ai fini', 'tu as fini', 'il/elle/on a fini', 'nous avons fini', 'vous avez fini', 'ils/elles ont fini'],
        'imparfait': ['je finissais', 'tu finissais', 'il/elle/on finissait', 'nous finissions', 'vous finissiez', 'ils/elles finissaient'],
        'futur simple': ['je finirai', 'tu finiras', 'il/elle/on finira', 'nous finirons', 'vous finirez', 'ils/elles finiront'],
        'conditionnel présent': ['je finirais', 'tu finirais', 'il/elle/on finirait', 'nous finirions', 'vous finiriez', 'ils/elles finiraient'],
        'passé simple': ['je finis', 'tu finis', 'il/elle/on finit', 'nous finîmes', 'vous finîtes', 'ils/elles finirent']
    },
    'choisir': {
        'présent': ['je choisis', 'tu choisis', 'il/elle/on choisit', 'nous choisissons', 'vous choisissez', 'ils/elles choisissent'],
        'passé composé': ['j\' ai choisi', 'tu as choisi', 'il/elle/on a choisi', 'nous avons choisi', 'vous avez choisi', 'ils/elles ont choisi'],
        'imparfait': ['je choisissais', 'tu choisissais', 'il/elle/on choisissait', 'nous choisissions', 'vous choisissiez', 'ils/elles choisissaient'],
        'futur simple': ['je choisirai', 'tu choisiras', 'il/elle/on choisira', 'nous choisirons', 'vous choisirez', 'ils/elles choisiront'],
        'conditionnel présent': ['je choisirais', 'tu choisirais', 'il/elle/on choisirait', 'nous choisirions', 'vous choisiriez', 'ils/elles choisiraient'],
        'passé simple': ['je choisis', 'tu choisis', 'il/elle/on choisit', 'nous choisîmes', 'vous choisîtes', 'ils/elles choisirent']
    },
    'grandir': {
        'présent': ['je grandis', 'tu grandis', 'il/elle/on grandit', 'nous grandissons', 'vous grandissez', 'ils/elles grandissent'],
        'passé composé': ['j\' ai grandi', 'tu as grandi', 'il/elle/on a grandi', 'nous avons grandi', 'vous avez grandi', 'ils/elles ont grandi'],
        'imparfait': ['je grandissais', 'tu grandissais', 'il/elle/on grandissait', 'nous grandissions', 'vous grandissiez', 'ils/elles grandissaient'],
        'futur simple': ['je grandirai', 'tu grandiras', 'il/elle/on grandira', 'nous grandirons', 'vous grandirez', 'ils/elles grandiront'],
        'conditionnel présent': ['je grandirais', 'tu grandirais', 'il/elle/on grandirait', 'nous grandirions', 'vous grandiriez', 'ils/elles grandiraient'],
        'passé simple': ['je grandis', 'tu grandis', 'il/elle/on grandit', 'nous grandîmes', 'vous grandîtes', 'ils/elles grandirent']
    },
    'réussir': {
        'présent': ['je réussis', 'tu réussis', 'il/elle/on réussit', 'nous réussissons', 'vous réussissez', 'ils/elles réussissent'],
        'passé composé': ['j\' ai réussi', 'tu as réussi', 'il/elle/on a réussi', 'nous avons réussi', 'vous avez réussi', 'ils/elles ont réussi'],
        'imparfait': ['je réussissais', 'tu réussissais', 'il/elle/on réussissait', 'nous réussissions', 'vous réussissiez', 'ils/elles réussissaient'],
        'futur simple': ['je réussirai', 'tu réussiras', 'il/elle/on réussira', 'nous réussirons', 'vous réussirez', 'ils/elles réussiront'],
        'passé simple': ['je réussis', 'tu réussis', 'il/elle/on réussit', 'nous réussîmes', 'vous réussîtes', 'ils/elles réussirent']
    },
    'remplir': {
        'présent': ['je remplis', 'tu remplis', 'il/elle/on remplit', 'nous remplissons', 'vous remplissez', 'ils/elles remplissent'],
        'passé composé': ['j\' ai rempli', 'tu as rempli', 'il/elle/on a rempli', 'nous avons rempli', 'vous avez rempli', 'ils/elles ont rempli'],
        'imparfait': ['je remplissais', 'tu remplissais', 'il/elle/on remplissait', 'nous remplissions', 'vous remplissiez', 'ils/elles remplissaient'],
        'futur simple': ['je remplirai', 'tu rempliras', 'il/elle/on remplira', 'nous remplirons', 'vous remplirez', 'ils/elles rempliront'],
        'conditionnel présent': ['je remplirais', 'tu remplirais', 'il/elle/on remplirait', 'nous remplirions', 'vous rempliriez', 'ils/elles rempliraient'],
        'passé simple': ['je remplis', 'tu remplis', 'il/elle/on remplit', 'nous remplîmes', 'vous remplîtes', 'ils/elles remplirent']
    },

    # Verbes du troisième groupe
    'être': {
        'présent': ['je suis', 'tu es', 'il/elle/on est', 'nous sommes', 'vous êtes', 'ils/elles sont'],
        'passé composé': ['j\' ai été', 'tu as été', 'il/elle/on a été', 'nous avons été', 'vous avez été', 'ils/elles ont été'],
        'imparfait': ['j\' étais', 'tu étais', 'il/elle/on était', 'nous étions', 'vous étiez', 'ils/elles étaient'],
        'futur simple': ['je serai', 'tu seras', 'il/elle/on sera', 'nous serons', 'vous serez', 'ils/elles seront'],
        'conditionnel présent': ['je serais', 'tu serais', 'il/elle/on serait', 'nous serions', 'vous seriez', 'ils/elles seraient'],
        'passé simple': ['je fus', 'tu fus', 'il/elle/on fut', 'nous fûmes', 'vous fûtes', 'ils/elles furent']
    },
    'avoir': {
        'présent': ['j\' ai', 'tu as', 'il/elle/on a', 'nous avons', 'vous avez', 'ils/elles ont'],
        'passé composé': ['j\' ai eu', 'tu as eu', 'il/elle/on a eu', 'nous avons eu', 'vous avez eu', 'ils/elles ont eu'],
        'imparfait': ['j\' avais', 'tu avais', 'il/elle/on avait', 'nous avions', 'vous aviez', 'ils/elles avaient'],
        'futur simple': ['j\' aurai', 'tu auras', 'il/elle/on aura', 'nous aurons', 'vous aurez', 'ils/elles auront'],
        'conditionnel présent': ['j\' aurais', 'tu aurais', 'il/elle/on aurait', 'nous aurions', 'vous auriez', 'ils/elles auraient'],
        'passé simple': ['j\' eus', 'tu eus', 'il/elle/on eut', 'nous eûmes', 'vous eûtes', 'ils/elles eurent']
    },
    'faire': {
        'présent': ['je fais', 'tu fais', 'il/elle/on fait', 'nous faisons', 'vous faites', 'ils/elles font'],
        'passé composé': ['j\' ai fait', 'tu as fait', 'il/elle/on a fait', 'nous avons fait', 'vous avez fait', 'ils/elles ont fait'],
        'imparfait': ['je faisais', 'tu faisais', 'il/elle/on faisait', 'nous faisions', 'vous faisiez', 'ils/elles faisaient'],
        'futur simple': ['je ferai', 'tu feras', 'il/elle/on fera', 'nous ferons', 'vous ferez', 'ils/elles feront'],
        'conditionnel présent': ['je ferais', 'tu ferais', 'il/elle/on ferait', 'nous ferions', 'vous feriez', 'ils/elles feraient'],
        'passé simple': ['je fis', 'tu fis', 'il/elle/on fit', 'nous fîmes', 'vous fîtes', 'ils/elles firent']
    },
    'dire': {
        'présent': ['je dis', 'tu dis', 'il/elle/on dit', 'nous disons', 'vous dites', 'ils/elles disent'],
        'passé composé': ['j\' ai dit', 'tu as dit', 'il/elle/on a dit', 'nous avons dit', 'vous avez dit', 'ils/elles ont dit'],
        'imparfait': ['je disais', 'tu disais', 'il/elle/on disait', 'nous disions', 'vous disiez', 'ils/elles disaient'],
        'futur simple': ['je dirai', 'tu diras', 'il/elle/on dira', 'nous dirons', 'vous direz', 'ils/elles diront'],
        'conditionnel présent': ['je dirais', 'tu dirais', 'il/elle/on dirait', 'nous dirions', 'vous diriez', 'ils/elles diraient'],
        'passé simple': ['je dis', 'tu dis', 'il/elle/on dit', 'nous dîmes', 'vous dîtes', 'ils/elles dirent']
    },
    'aller': {
        'présent': ['je vais', 'tu vas', 'il/elle/on va', 'nous allons', 'vous allez', 'ils/elles vont'],
        'passé composé': ['je suis allé', 'tu es allé', 'il/elle/on est allé', 'nous sommes allés', 'vous êtes allés', 'ils/elles sont allés'],
        'imparfait': ['j\' allais', 'tu allais', 'il/elle/on allait', 'nous allions', 'vous alliez', 'ils/elles allaient'],
        'futur simple': ['j\' irai', 'tu iras', 'il/elle/on ira', 'nous irons', 'vous irez', 'ils/elles iront'],
        'conditionnel présent': ['j\' irais', 'tu irais', 'il/elle/on irait', 'nous irions', 'vous iriez', 'ils/elles iraient'],
        'passé simple': ['j\' allai', 'tu allas', 'il/elle/on alla', 'nous allâmes', 'vous allâtes', 'ils/elles allèrent']
    },

    "voir": {
        "présent": ["je vois", "tu vois", "il/elle/on voit", "nous voyons", "vous voyez", "ils/elles voient"],
        "passé composé": ["j\' ai vu", "tu as vu", "il/elle/on a vu", "nous avons vu", "vous avez vu", "ils/elles ont vu"],
        "imparfait": ["je voyais", "tu voyais", "il/elle/on voyait", "nous voyions", "vous voyiez", "ils/elles voyaient"],
        "futur simple": ["je verrai", "tu verras", "il/elle/on verra", "nous verrons", "vous verrez", "ils/elles verront"],
        "conditionnel présent": ["je verrais", "tu verrais", "il/elle/on verrait", "nous verrions", "vous verriez", "ils/elles verraient"],
        "passé simple": ["je vis", "tu vis", "il/elle/on vit", "nous vîmes", "vous vîtes", "ils/elles virent"]
    },
    "savoir": {
        "présent": ["je sais", "tu sais", "il/elle/on sait", "nous savons", "vous savez", "ils/elles savent"],
        "passé composé": ["j\' ai su", "tu as su", "il/elle/on a su", "nous avons su", "vous avez su", "ils/elles ont su"],
        "imparfait": ["je savais", "tu savais", "il/elle/on savait", "nous savions", "vous saviez", "ils/elles savaient"],
        "futur simple": ["je saurai", "tu sauras", "il/elle/on saura", "nous saurons", "vous saurez", "ils/elles sauront"],
        "conditionnel présent": ["je saurais", "tu saurais", "il/elle/on saurait", "nous saurions", "vous sauriez", "ils/elles sauraient"],
        "passé simple": ["je sus", "tu sus", "il/elle/on sut", "nous sûmes", "vous sûtes", "ils/elles surent"]
    },
    "pouvoir": {
        "présent": ["je peux", "tu peux", "il/elle/on peut", "nous pouvons", "vous pouvez", "ils/elles peuvent"],
        "passé composé": ["j\' ai pu", "tu as pu", "il/elle/on a pu", "nous avons pu", "vous avez pu", "ils/elles ont pu"],
        "imparfait": ["je pouvais", "tu pouvais", "il/elle/on pouvait", "nous pouvions", "vous pouviez", "ils/elles pouvaient"],
        "futur simple": ["je pourrai", "tu pourras", "il/elle/on pourra", "nous pourrons", "vous pourrez", "ils/elles pourront"],
        "conditionnel présent": ["je pourrais", "tu pourrais", "il/elle/on pourrait", "nous pourrions", "vous pourriez", "ils/elles pourraient"],
        "passé simple": ["je pus", "tu pus", "il/elle/on put", "nous pûmes", "vous pûtes", "ils/elles purent"]
    },
    "vouloir": {
        "présent": ["je veux", "tu veux", "il/elle/on veut", "nous voulons", "vous voulez", "ils/elles veulent"],
        "passé composé": ["j\' ai voulu", "tu as voulu", "il/elle/on a voulu", "nous avons voulu", "vous avez voulu", "ils/elles ont voulu"],
        "imparfait": ["je voulais", "tu voulais", "il/elle/on voulait", "nous voulions", "vous vouliez", "ils/elles voulaient"],
        "futur simple": ["je voudrai", "tu voudras", "il/elle/on voudra", "nous voudrons", "vous voudrez", "ils/elles voudront"],
        "conditionnel présent": ["je voudrais", "tu voudrais", "il/elle/on voudrait", "nous voudrions", "vous voudriez", "ils/elles voudraient"],
        "passé simple": ["je voulus", "tu voulus", "il/elle/on voulut", "nous voulûmes", "vous voulûtes", "ils/elles voulurent"]
    },
    "venir": {
        "présent": ["je viens", "tu viens", "il/elle/on vient", "nous venons", "vous venez", "ils/elles viennent"],
        "passé composé": ["je suis venu", "tu es venu", "il/elle/on est venu", "nous sommes venus", "vous êtes venus", "ils/elles sont venus"],
        "imparfait": ["je venais", "tu venais", "il/elle/on venait", "nous venions", "vous veniez", "ils/elles venaient"],
        "futur simple": ["je viendrai", "tu viendras", "il/elle/on viendra", "nous viendrons", "vous viendrez", "ils/elles viendront"],
        "conditionnel présent": ["je viendrais", "tu viendrais", "il/elle/on viendrait", "nous viendrions", "vous viendriez", "ils/elles viendraient"],
        "passé simple": ["je vins", "tu vins", "il/elle/on vint", "nous vînmes", "vous vîntes", "ils/elles vinrent"]
    },
    "prendre": {
        "présent": ["je prends", "tu prends", "il/elle/on prend", "nous prenons", "vous prenez", "ils/elles prennent"],
        "passé composé": ["j\' ai pris", "tu as pris", "il/elle/on a pris", "nous avons pris", "vous avez pris", "ils/elles ont pris"],
        "imparfait": ["je prenais", "tu prenais", "il/elle/on prenait", "nous prenions", "vous preniez", "ils/elles prenaient"],
        "futur simple": ["je prendrai", "tu prendras", "il/elle/on prendra", "nous prendrons", "vous prendrez", "ils/elles prendront"],
        "conditionnel présent": ["je prendrais", "tu prendrais", "il/elle/on prendrait", "nous prendrions", "vous prendriez", "ils/elles prendraient"],
        "passé simple": ["je pris", "tu pris", "il/elle/on prit", "nous prîmes", "vous prîtes", "ils/elles prirent"]
    },
    "devoir": {
        "présent": ["je dois", "tu dois", "il/elle/on doit", "nous devons", "vous devez", "ils/elles doivent"],
        "passé composé": ["j\' ai dû", "tu as dû", "il/elle/on a dû", "nous avons dû", "vous avez dû", "ils/elles ont dû"],
        "imparfait": ["je devais", "tu devais", "il/elle/on devait", "nous devions", "vous deviez", "ils/elles devaient"],
        "futur simple": ["je devrai", "tu devras", "il/elle/on devra", "nous devrons", "vous devrez", "ils/elles devront"],
        "conditionnel présent": ["je devrais", "tu devrais", "il/elle/on devrait", "nous devrions", "vous devriez", "ils/elles devraient"],
        "passé simple": ["je dus", "tu dus", "il/elle/on dut", "nous dûmes", "vous dûtes", "ils/elles durent"]
    },
    "mettre": {
        "présent": ["je mets", "tu mets", "il/elle/on met", "nous mettons", "vous mettez", "ils/elles mettent"],
        "passé composé": ["j\' ai mis", "tu as mis", "il/elle/on a mis", "nous avons mis", "vous avez mis", "ils/elles ont mis"],
        "imparfait": ["je mettais", "tu mettais", "il/elle/on mettait", "nous mettions", "vous mettiez", "ils/elles mettaient"],
        "futur simple": ["je mettrai", "tu mettras", "il/elle/on mettra", "nous mettrons", "vous mettrez", "ils/elles mettront"],
        "conditionnel présent": ["je mettrais", "tu mettrais", "il/elle/on mettrait", "nous mettrions", "vous mettriez", "ils/elles mettraient"],
        "passé simple": ["je mis", "tu mis", "il/elle/on mit", "nous mîmes", "vous mîtes", "ils/elles mirent"]
    },
    "lire": {
        "présent": ["je lis", "tu lis", "il/elle/on lit", "nous lisons", "vous lisez", "ils/elles lisent"],
        "passé composé": ["j\' ai lu", "tu as lu", "il/elle/on a lu", "nous avons lu", "vous avez lu", "ils/elles ont lu"],
        "imparfait": ["je lisais", "tu lisais", "il/elle/on lisait", "nous lisions", "vous lisiez", "ils/elles lisaient"],
        "futur simple": ["je lirai", "tu liras", "il/elle/on lira", "nous lirons", "vous lirez", "ils/elles liront"],
        "conditionnel présent": ["je lirais", "tu lirais", "il/elle/on lirait", "nous lirions", "vous liriez", "ils/elles liraient"],
        "passé simple": ["je lus", "tu lus", "il/elle/on lut", "nous lûmes", "vous lûtes", "ils/elles lurent"]
    },
    "écrire": {
        "présent": ["j\' écris", "tu écris", "il/elle/on écrit", "nous écrivons", "vous écrivez", "ils/elles écrivent"],
        "passé composé": ["j\' ai écrit", "tu as écrit", "il/elle/on a écrit", "nous avons écrit", "vous avez écrit", "ils/elles ont écrit"],
        "imparfait": ["j\' écrivais", "tu écrivais", "il/elle/on écrivait", "nous écrivions", "vous écriviez", "ils/elles écrivaient"],
        "futur simple": ["j\' écrirai", "tu écriras", "il/elle/on écrira", "nous écrirons", "vous écrirez", "ils/elles écriront"],
        "conditionnel présent": ["j\' écrirais", "tu écrirais", "il/elle/on écrirait", "nous écririons", "vous écririez", "ils/elles écriraient"],
        "passé simple": ["j\' écrivis", "tu écrivis", "il/elle/on écrivit", "nous écrivîmes", "vous écrivîtes", "ils/elles écrivirent"]
    },
    "dire": {
        "présent": ["je dis", "tu dis", "il/elle/on dit", "nous disons", "vous dites", "ils/elles disent"],
        "passé composé": ["j\' ai dit", "tu as dit", "il/elle/on a dit", "nous avons dit", "vous avez dit", "ils/elles ont dit"],
        "imparfait": ["je disais", "tu disais", "il/elle/on disait", "nous disions", "vous disiez", "ils/elles disaient"],
        "futur simple": ["je dirai", "tu diras", "il/elle/on dira", "nous dirons", "vous direz", "ils/elles diront"],
        "conditionnel présent": ["je dirais", "tu dirais", "il/elle/on dirait", "nous dirions", "vous diriez", "ils/elles diraient"],
        "passé simple": ["je dis", "tu dis", "il/elle/on dit", "nous dîmes", "vous dîtes", "ils/elles dirent"]
    },

    "partir": {
        "présent": ["je pars", "tu pars", "il/elle/on part", "nous partons", "vous partez", "ils/elles partent"],
        "passé composé": ["je suis parti", "tu es parti", "il/elle/on est parti", "nous sommes partis", "vous êtes partis", "ils/elles sont partis"],
        "imparfait": ["je partais", "tu partais", "il/elle/on partait", "nous partions", "vous partiez", "ils/elles partaient"],
        "futur simple": ["je partirai", "tu partiras", "il/elle/on partira", "nous partirons", "vous partirez", "ils/elles partiront"],
        "conditionnel présent": ["je partirais", "tu partirais", "il/elle/on partirait", "nous partirions", "vous partiriez", "ils/elles partiraient"],
        "passé simple": ["je partis", "tu partis", "il/elle/on partit", "nous partîmes", "vous partîtes", "ils/elles partirent"]
    },
    "courir": {
        "présent": ["je cours", "tu cours", "il/elle/on court", "nous courons", "vous courez", "ils/elles courent"],
        "passé composé": ["j\' ai couru", "tu as couru", "il/elle/on a couru", "nous avons couru", "vous avez couru", "ils/elles ont couru"],
        "imparfait": ["je courais", "tu courais", "il/elle/on courait", "nous courions", "vous couriez", "ils/elles couraient"],
        "futur simple": ["je courrai", "tu courras", "il/elle/on courra", "nous courrons", "vous courrez", "ils/elles courront"],
        "conditionnel présent": ["je courrais", "tu courrais", "il/elle/on courrait", "nous courrions", "vous courriez", "ils/elles courraient"],
        "passé simple": ["je courus", "tu courus", "il/elle/on courut", "nous courûmes", "vous courûtes", "ils/elles coururent"]
    },
    "mourir": {
        "présent": ["je meurs", "tu meurs", "il/elle/on meurt", "nous mourons", "vous mourez", "ils/elles meurent"],
        "passé composé": ["je suis mort", "tu es mort", "il/elle/on est mort", "nous sommes morts", "vous êtes morts", "ils/elles sont morts"],
        "imparfait": ["je mourais", "tu mourais", "il/elle/on mourait", "nous mourions", "vous mouriez", "ils/elles mouraient"],
        "futur simple": ["je mourrai", "tu mourras", "il/elle/on mourra", "nous mourrons", "vous mourrez", "ils/elles mourront"],
        "conditionnel présent": ["je mourrais", "tu mourrais", "il/elle/on mourrait", "nous mourrions", "vous mourriez", "ils/elles mourraient"],
        "passé simple": ["je mourus", "tu mourus", "il/elle/on mourut", "nous mourûmes", "vous mourûtes", "ils/elles moururent"]
    }
}


verbes = list(conjugaisons.keys())

# Fonction pour choisir un verbe et un temps au hasard

utilise = set()
dernier_verbe = None
dernier_temps = None


def choisir_exercice():
    global utilise, dernier_verbe, dernier_temps

    combinaisons_possibles = [(verbe, temps)
                              for verbe in verbes for temps in conjugaisons[verbe]]

    if len(utilise) == len(combinaisons_possibles):
        utilise = set()
        dernier_verbe = None
        dernier_temps = None

    while True:
        verbe = random.choice(verbes)
        temps = random.choice(list(conjugaisons[verbe].keys()))
        if (verbe, temps) not in utilise and temps != dernier_temps and verbe != dernier_verbe:
            utilise.add((verbe, temps))
            dernier_verbe = verbe
            dernier_temps = temps
            return verbe, temps


def exercice():
    points = 0
    verbe, temps = choisir_exercice()
    print(f"Conjugue le verbe '{verbe}' au temps '{temps}':")

    # Afficher la réponse correcte pour chaque personne
    for i, personne in enumerate(['je', 'tu', 'il/elle/on', 'nous', 'vous', 'ils/elles']):
        reponse = input(f"{personne} : ")
        verification = conjugaisons[verbe][temps][i].split()
        if len(verification) == 2:
            if reponse.strip().lower() == verification[1].lower():
                console.print("Correct!", style="bold green")
                points += 1
            else:
                console.print(
                    f"Incorrect. La bonne réponse est: {verification[1]}", style="bold red")
        elif len(verification) > 2:
            if reponse.strip().lower() == f'{verification[1].lower()} {verification[2].lower()}':
                console.print("Correct!", style="bold green")
                points += 1
            else:
                console.print(
                    f"Incorrect. La bonne réponse est: {verification[1].lower()} {verification[2].lower()}", style="bold red")

    return points


def main():
    total_points = 0
    while total_points < 100:
        points = exercice()
        total_points += points
        console.print(
            f"Votre score actuel est : {total_points} points.", style="bold purple")
        if total_points >= 100:
            console.print(
                "Félicitations, vous avez atteint 100 points!", style="bold green")
            break


if __name__ == "__main__":
    main()
