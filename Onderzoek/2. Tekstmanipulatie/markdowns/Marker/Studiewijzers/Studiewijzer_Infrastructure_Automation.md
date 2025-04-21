# Infrastructure Automation (2024-2025) (CURLINKEDINFRA2024) Studiewijzer Infrastructure Automation (2024-2025)

## Inhoudsopgave

- 1. Doel en plaats van de cursus in het curriculum
- 2. Leerdoelen en competenties
- 3. Leerinhoud
- 4. Leermateriaal
- 5. Werkvormen
- 6. Werk- en leeraanwijzingen
- 7. Studiebegeleiding
- 8. Planning
- 9. Evaluatie

# Studiewijzer Infrastructure Automation (2024-2025) (Leerpad)

Deze studiewijzer geldt zowel voor de reguliere studenten als de studenten afstandsleren (TIAO). Waar nodig wordt duidelijk onderscheid gemaakt tussen zaken die enkel voor één van deze twee groepen gelden. Wat betreft praktische afspraken, regelingen, verwachtingen, enz. in verband met deze cursus zijn de enige geldige bronnen van informatie:

- De studiecheche van dit opleidingsonderdeel, te bekijken via de Chamilo- cursus of [https://hogent.be/studieches/](https://hogent.be/studiefiches/) [\(https://hogent.be/studieches/\)](https://hogent.be/studiefiches/);
- Deze studiewijzer;
- Documenten op Chamilo;
- Aankondigingen op Chamilo—deze worden ook telkens per e-mail naar de betrokken studenten gestuurd;
- Het Onderwijs- en [Examenreglement](https://www.hogent.be/student/een-vlotte-start/onderwijs-en-examenregeling/) (OER) [\(https://www.hogent.be/student/een](https://www.hogent.be/student/een-vlotte-start/onderwijs-en-examenregeling/)[vlotte-start/onderwijs-en-examenregeling/\)](https://www.hogent.be/student/een-vlotte-start/onderwijs-en-examenregeling/), incl. departementale aanvullingen (DOER).

Jullie zijn zelf verantwoordelijk voor het opvolgen en lezen van alle aankondigingen. Studenten worden geacht hun opleidingsgerelateerde e-mails regelmatig op te volgen.

Indien er ergens twijfel over bestaat, of er is iets niet duidelijk, neem dan zo snel mogelijk contact op met je lector. De aangewezen manieren worden opgesomd in Sectie Studiebegeleiding.

De ervaring leert dat de onderlinge communicatie tussen studenten via andere platformen enkel leidt tot verwarring, foute informatie en overbodige discussie. Gebruik dus a.u.b. de ociële kanalen, dat is de enige garantie op een open en correcte communicatie rond deze cursus.

## 1. Doel en plaats van de cursus in het curriculum (Pagina)

Deze cursus biedt een inleiding in het vakgebied Infrastructure Automation, d.w.z. het geautomatiseerd opzetten en in productie brengen van reproduceerbare en schaalbare netwerkdiensten.

Klassiek werden (en worden) servers stap voor stap handmatig geïnstalleerd en gecongureerd. Hopelijk houdt de systeembeheerder daarbij een gedetailleerde procedurehandleiding bij zodat dit werk kan gereproduceerd worden, bijvoorbeeld als de servercapaciteit moet uitgebreid worden, als er moet gemigreerd worden naar een nieuwere versie van het besturingssysteem, enz. Wanneer je als systeembeheerder een serverpark van tientallen, honderden of zelfs duizenden machines (hetzij fysiek, hetzij virtueel) moet beheren, dan is het manueel opzetten, of zelfs scripten van de conguratie niet meer voldoende. In dit soort omgevingen wordt steevast gebruik gemaakt van Conguration Management Systems om de taaklast beheersbaar te houden.

In deze cursus maken we gebruik van het Conguration Management System [Ansible](https://www.ansible.com/) [\(https://www.ansible.com\)](https://www.ansible.com/), omdat dit een voor beginners toegankelijk systeem is dat qua losoe en logica aansluit bij klassieke shell scripts. In het werkveld is de kans groot dat je ook met andere Conguration Management Systems in aanraking komt, bijvoorbeeld [Puppet](https://puppet.com/) [\(https://puppet.com/\)](https://puppet.com/) of [Chef](https://www.chef.io/) [\(https://www.chef.io/\)](https://www.chef.io/).

Andere termen die gebruikt worden in plaats van Infrastructure Automation:

- Infrastructure as Code: de sleutel tot automatiseren bestaat er in om de gewenste toestand van een systeem precies te beschrijven in een daarvoor ontworpen taal. Puppet heeft hiervoor bijvoorbeeld een Domain Specic Language (DSL) ontwikkeld, terwijl Ansible gebruik maakt van een bestaande taal voor het beschrijven van gestructureerde data, nl. [YAML](https://yaml.org/) [\(https://yaml.org/\)](https://yaml.org/). Deze beschrijving is uitvoerbaar (executable), d.w.z. een conguration management system kan aan de hand van deze beschrijving een systeem naar de gewenste toestand brengen. Je kan dit beschouwen als (bron)code, maar in plaats van software bouw je er infrastructuur mee. Dit brengt als bijkomend voordeel met zich mee dat allerlei best-practices uit softwareontwikkeling op die manier ook kunnen toegepast worden in systeembeheer: code bijhouden in een versiebeheersysteem, codeerstijl toepassen, geautomatiseerd testen, geautomatiseerd uitrollen van infrastructuur (CI/CD), enz.
- GitOps: tegenwoordig hou je broncode zo goed als altijd bij in een versiebeheersysteem. Git is in dit domein marktleider geworden. Daarom wordt het bijhouden van infrastructuur-code in Git soms ook GitOps genoemd.
- De term Infrastructure Automation wordt vaak verward met DevOps. DevOps is de naam van de professionele beweging (ontstaan in 2009 in [Gent](https://legacy.devopsdays.org/events/2009-ghent/) [\(https://legacy.devopsdays.org/events/2009-ghent/\)](https://legacy.devopsdays.org/events/2009-ghent/)) die software-ontwikkelaars (DEVelopers) en systeembeheerders (OPerationS) nauwer wil laten samenwerken met als doel kwalitatievere software. In een klassieke IT-organisatiestructuur zijn softwareontwikkeling en infrastructuur (= systeem- en netwerkbeheer) aparte afdelingen met hun eigen hiërarchie, manier van budgetteren, operationele doelstellingen, enz. Dat leidt tot allerlei kwaliteitsproblemen. Door de bedrijfsstructuur te organiseren rond interdisciplinaire product-teams, komt men tot een betere samenwerking, gedeelde verantwoordelijkheid en gemeenschappelijke doelstellingen. DevOps is dus een term die eerder te maken heeft met bedrijfscultuur en -organisatie dan met technische onderwerpen. Het is wel zo dat een verregaande automatisering typisch is voor DevOps-teams, en wellicht is de verwarring zo ontstaan.

Binnen het curriculum situeert deze cursus zich in het keuzepakket System and Network Administrator van het derde modeltraject. Qua inhoud gaat het verder op de olods Linux en System Engineering Projectuit het 2e modeltraject.

De kennis en vaardigheden die je in Infrastructure Automation opdoet, kan je ook toepassen in DevOps project: Operations.

## 2. Leerdoelen en competenties (Pagina)

Na het succesvol afwerken van deze cursus:

- Kan je het opzetten van netwerkservices automatiseren met een conguration management system
- Kan je reproduceerbare virtuele omgevingen installeren en congureren (Infrastructure as Code) met geschikte tools voor de automatisering van de gehele levenscyclus van een VM (bv. Vagrant, Docker Compose ...)
- Kan je een orchestratiesysteem voor containervirtualisatie congureren en beheren (bv. Kubernetes)
- Kan je de werking van een it-systeem opvolgen met een logging- of monitoringsysteem om defecten te detecteren en de oorzaak op te sporen

## **Vereiste voorkennis**

We verwachten een gemiddelde vaardigheid in Linux system administration:

- Installatie van software en basis commando's
- Beheer van gebruikers en permissies
- Installatie van netwerkservices (bv. Apache, BIND, DHCP, etc.)
- Beheer van netwerkservices met systemd
- Beheer van rewall met rewall-cmd
- Bash scripting
- Systematische troubleshooting-methodologie (bottom-up methode)

Je bent ook vaardig met Git en GitHub.

# 3. Leerinhoud (Pagina)

- Inleiding, opzetten werkomgeving
- Module 1: continuous integration/delivery Een CI/CD pipeline opzetten met Jenkins
- Module 2: conguration management
	- Geautomatiseerd opzetten van netwerk- en serverinfrastructuur met Ansible
- Module 3: container orchestration Applicaties in containers uitrollen in een productiewaardige omgeving met
	- Kubernetes
- Module 4: monitoring
	- Opvolging van de werking van ict-infrastructuur met Prometheus

## 4. Leermateriaal (Pagina)

Het leermateriaal voor deze cursus bestaat uit:

- De informatie op Chamilo, o.a. deze studiewijzer
- Een leerpad met een gestructureerd overzicht van de gehele vakinhoud met
- instructies voor installatie van nodige software en opstarten van de laboopdrachten
	- links naar het relevante studiemateriaal
		- Slides gebruikt bij de klassikale instructie
		- On-line handleidingen van de gebruikte software
		- Lesopnames (voor zover beschikbaar)
		- Achtergrondinformatie zoals e-boeken, online cursussen die verder ingaan op de aangehaalde onderwerpen, enz.
- Opgave van de labo-oefeningen (op Github)

Bovenaan de intro-pagina van deze cursus vind je een hoofding met links naar de relevante content.

Je kan je basiskennis Linux opfrissen via het linux-training-hogent lesmateriaal: <https://hogenttin.github.io/linux-training-hogent/> [\(https://hogenttin.github.io/linux-training-hogent/\)](https://hogenttin.github.io/linux-training-hogent/) Voor jullie is vooral "Introduction to Linux" en "Linux for Operations" het interessantst.

#### **Opmerking**

Deze cursus werd tot academiejaar 2023-2024 ook in het Engels aangeboden. Omdat het praktisch niet haalbaar is om al het cursusmateriaal in het Nederlands én Engels te ontwikkelen en onderhouden, is een deel van het materiaal momenteel enkel in het Engels beschikbaar.

# 5. Werkvormen (Pagina)

In dit opleidingsonderdeel wordt hoofdzakelijk gewerkt aan de hand van labo-opdrachten. De ondersteunende studiematerialen moeten je in staat stellen die met succes af te werken.

# **Reguliere studenten**

Tijdens de reguliere contactmomenten geeft de lector klassikaal instructie, waarna studenten zelfstandig werken aan de labo-opdrachten. Studenten tonen tussentijdse resultaten tijdens een voortgangsgesprek aan de lector en kunnen dan uitleg vragen bij specieke problemen.

# **Afstandsleren**

Studenten afstandsleren verwerken de leerstof op eigen tempo, aan de hand van de aangeboden studiematerialen, en voeren de labo-opdrachten uit. Het leerpad met het overzicht van de leerinhoud biedt daarbij een eerste houvast.

Ze kunnen op de contactmomenten voor studenten afstandsleren een afspraak maken met de lector voor een individueel voortgangsgesprek en opvolging (zie Studiebegeleiding).

## 6. Werk- en leeraanwijzingen (Pagina)

Het werken met labo-opdrachten vergt een zekere mate van zelfstandigheid van jou als student, maar dat is precies ook een attitude die verwacht wordt van een systeembeheerder. Je neemt dus zelf initiatief om de nodige kennis te vergaren en zoekt naar oplossingen voor de problemen die je ongetwijfeld zal tegenkomen.

Help elkaar daarin: samenwerken en kennis delen wordt van harte aangemoedigd. De lector is uiteraard beschikbaar om je bij te staan als je vast komt te zitten en kan je tips geven of verwijzen naar geschikte aanvullende studiematerialen.

Reguliere studenten moeten in de loop van het semester minstens drie keer persoonlijk bij de lector langs komen om deelresultaten te tonen. Kom zeker langs als je ergens vast zit, zodat de lector je terug op weg kan helpen!

## 7. Studiebegeleiding (Pagina)

## **Begeleiding reguliere studenten**

Reguliere studenten kunnen tijdens de contactmomenten bij de lector terecht voor individuele opvolging en voor het opleveren van deelresultaten.

Ook als je weinig tot niets gerealiseerd hebt, ga je best eens langs! Dat is immers een teken dat je ergens vast zit, en de lector kan je dan opnieuw op weg helpen.

## **Begeleiding afstandsstudenten**

Studenten afstandsleren kunnen op verschillende manieren rekenen op begeleiding:

Via het Teams-kanaal (zie hieronder),

Neem contact op met [bert.vanvreckem@hogent.be](mailto:bert.vanvreckem@hogent.be?subject=%5BInfra-TIAO%5D%20Afspraak%20voor%20individuele%20opvolging&body=Beste%20meneer%20Van%20Vreckem%2C%0A%0AINHOUD%20BERICHT%0A%0AMet%20vriendelijke%20groet%2C%0A%0ANAAM) [\(mailto:bert.vanvreckem@hogent.be?subject=%5BInfra-](mailto:bert.vanvreckem@hogent.be?subject=%5BInfra-TIAO%5D%20Afspraak%20voor%20individuele%20opvolging&body=Beste%20meneer%20Van%20Vreckem%2C%0A%0AINHOUD%20BERICHT%0A%0AMet%20vriendelijke%20groet%2C%0A%0ANAAM)[TIAO%5D%20Afspraak%20voor%20individuele%20opvolging&body=Beste%20meneer%20Van%20Vreckem%2C%0A](mailto:bert.vanvreckem@hogent.be?subject=%5BInfra-TIAO%5D%20Afspraak%20voor%20individuele%20opvolging&body=Beste%20meneer%20Van%20Vreckem%2C%0A%0AINHOUD%20BERICHT%0A%0AMet%20vriendelijke%20groet%2C%0A%0ANAAM) om een afspraak te maken voor individuele opvolging.. Geef aub meteen een aantal mogelijkheden die voor jou passen (bij voorkeur ma-vr, overdag of 's avonds).

### **Vragen stellen**

Indien je vragen hebt over de inhoud van de cursus, of twijfelt over/vastzit bij een oefening, blijf daar dan niet mee zitten en vraag hulp!

Klik in de banner bovenaan de intro-pagina van de cursus op de rechtse tegel. Je komt dan terecht in het algemene team voor deze cursus. Stel je vraag in het daartoe bestemde kanaal, maar kijk eerst eens of je vraag (en het antwoord erop) er al niet staat. Als je het antwoord kent op de vraag van een medestudent, dan waarderen we ook als je daar op antwoordt.

Heb je een vraag die persoonlijk van aard is of niet relevant is voor andere studenten?

- Studenten dagonderwijs spreken best hun begeleidende lector aan tijdens de contactmomenten.
- Studenten afstandsleren kunnen een afspraak maken voor een contactmoment. Typisch gaat dit door via Teams.
- De lectoren persoonlijk contacteren via e-mail of Teams doe je enkel als het echt nodig is.
- In geen geval is het ok om de lectoren via Teams op te bellen voor een spraak- of video-oproep. Als dit nodig is zullen de lectoren met jou een Teams-gesprek inplannen op een vooraf afgesproken moment.

Hou er rekening mee dat de lectoren niet dagelijks kunnen antwoorden op vragen! Ook tijdens een vakantie of reces mag je niet rekenen op een antwoord.

### **Contactinformatie lectoren**

Zoals je hierboven kan lezen stel je vragen over dit vak tijdens de contactmomenten of via Teams. Contacteer ons enkel via mail voor persoonlijke aangelegenheden.

- Bert Van Vreckem ([bert.vanvreckem@hogent.be](mailto:bert.vanvreckem@hogent.be?subject=%5BInfra%5D%20ONDERWERP&body=Beste%20meneer%20Van%20Vreckem%0A%0ABERICHT%0A%0AMet%20vriendelijke%20groet%2C%0A%0ANAAM%0AKLASGROEP) [\(mailto:bert.vanvreckem@hogent.be?](mailto:bert.vanvreckem@hogent.be?subject=%5BInfra%5D%20ONDERWERP&body=Beste%20meneer%20Van%20Vreckem%0A%0ABERICHT%0A%0AMet%20vriendelijke%20groet%2C%0A%0ANAAM%0AKLASGROEP) [subject=%5BInfra%5D%20ONDERWERP&body=Beste%20meneer%20Van%20Vreckem%0A%0ABERICHT%0A%0AMet](mailto:bert.vanvreckem@hogent.be?subject=%5BInfra%5D%20ONDERWERP&body=Beste%20meneer%20Van%20Vreckem%0A%0ABERICHT%0A%0AMet%20vriendelijke%20groet%2C%0A%0ANAAM%0AKLASGROEP) vaktitularis, Aalst, contactpersoon afstandsleren (TIAO)
- Thomas Parmentier ([thomas.parmentier@hogent.be](mailto:thomas.parmentier@hogent.be?subject=%5BInfra%5D%20ONDERWERP&body=Beste%20meneer%20Parmentier%0A%0ABERICHT%0A%0AMet%20vriendelijke%20groeten%0ANAAM%0AKLASGROEP) [\(mailto:thomas.parmentier@hogent.be?](mailto:thomas.parmentier@hogent.be?subject=%5BInfra%5D%20ONDERWERP&body=Beste%20meneer%20Parmentier%0A%0ABERICHT%0A%0AMet%20vriendelijke%20groeten%0ANAAM%0AKLASGROEP) [subject=%5BInfra%5D%20ONDERWERP&body=Beste%20meneer%20Parmentier%0A%0ABERICHT%0A%0AMet%20v](mailto:thomas.parmentier@hogent.be?subject=%5BInfra%5D%20ONDERWERP&body=Beste%20meneer%20Parmentier%0A%0ABERICHT%0A%0AMet%20vriendelijke%20groeten%0ANAAM%0AKLASGROEP) Gent

### **Tip**

Het geeft altijd een slechte indruk als je niet lijkt te weten bij welke lector je in principe de lessen moet bijwonen...

# 8. Planning (Sectie)

# **Weekplanning**

Volgende weekplanning is enkel bij benadering! Wanneer er lessen wegvallen, bijvoorbeeld door verlofdagen, kunnen er nog verschuivingen gebeuren.

- In de weken waar een speciek onderwerp opgegeven staat, is er klassikale instructie voorzien over dat onderwerp.
- Tijdens de weken waar niets staat, is er ruimte voor het werken aan de laboopdrachten, individuele opvolging en het tonen van tussentijdse resultaten.
- In verband met de deadlines (in het rood):
	- Persoonlijke demo's worden ten laatste gegeven tijdens het contactmoment in de opgegeven week
	- Panopto-opnamen voor M1 (CI/CD), M3 (Kubernetes) worden ten laatste doorgestuurd op de zondag die de opgegeven week afsluit

|    | LesweekOnderwerp                                                        |
|----|-------------------------------------------------------------------------|
| 1  | Inleiding, praktische afspraken                                         |
|    | Installatie software                                                    |
|    | M1. CI/CD with Jenkins                                                  |
| 2  |                                                                         |
| 3  | M2. Conguration Management with Ansible                                 |
| 4  |                                                                         |
| 5  | Deadline afwerken en demonstreren M1 (CI/CD)                            |
| 6  |                                                                         |
| 7  | M3. Container Orchestration with Kubernetes                             |
| 8  |                                                                         |
| 9  |                                                                         |
| 10 | M4. Monitoring with Prometheus                                          |
| 11 |                                                                         |
| 12 | Deadline afwerken en demonstreren M3 (Kubernetes)                       |
|    | (Eventuele inhaalsessie, indien aangeboden door je lector)              |
| 13 | Woensdag 18 december: Deadline indienen Panopto-opnamen met demo's (M2, |
|    | M4)                                                                     |

# 9. Evaluatie (Pagina)

De evaluatie van dit opleidingsonderdeel gebeurt volledig via permanente evaluatie. Meer bepaald word je beoordeeld op de manier waarop je de opgegeven labo-opdrachten hebt uitgevoerd.

Je wordt geëvalueerd op basis van een portfolio dat je samenstelt tijdens de loop van het semester en dat je op een evaluatiemoment tijdens de examenperiode komt verdedigen. Dat portfolio bestaat concreet uit volgende elementen:

- De broncode, door elke student bijgehouden in een toegewezen Git repository
- Gedetailleerde labo-verslagen, eveneens bijgehouden in Git
- Demonstratie van deelresultaten aan de lector tijdens het semester, hetzij tijdens de contactmomenten, hetzij via een Panopto-opname
- Demonstratie van het eindresultaat aan de lector op het mondelinge evaluatiemoment tijdens de examenperiode, via een Teams-meeting (20min).

De toekenning van het examencijfer gebeurt op basis van "rubrics" die beschreven worden in de evaluatiekaart die gepubliceerd is op Chamilo, onder Documenten.

In een tabel worden een aantal criteria opgesomd, waar je aan moet voldoen. Je kan "voldoen" op verschillende niveaus, meer bepaald "bekwaam", "gevorderd", "deskundig", of in het slechtste geval "nog niet bekwaam". In de evaluatiekaart wordt beschreven wat je precies moet doen om elk niveau te behalen.

Om te slagen voor dit vak moet je aantonen dat je voor alle technische criteria minstens "bekwaam" bent. Met andere woorden, zelfs als je voor slechts één criterium "nog niet bekwaam" bevonden wordt, kan je niet slagen, hoe goed je ook de andere modules hebt afgewerkt. De niet-technische criteria (bv. rapportering) kunnen het examencijfer afhankelijk van het behaalde niveau nog positief of negatief beïnvloeden (en eventueel zelfs nog onder 10/20 doen zakken!).

#### **Let op!**

Merk op dat je zowel een werkend product moet opleveren (= broncode) als de verslagen indienen én demo's geven. Als één van de deliverables ontbreekt, wordt de opdracht beschouwd als niet gerealiseerd.

## **Demonstreren van labo's**

Van elk labo moet je de correcte werking demonstreren. Dat gebeurt voor de reguliere studenten in principe on-campus tijdens de contactmomenten. Studenten afstandsleren nemen een screencast op via Panopto en delen die met de begeleidende lector.

Wanneer je klaar bent met een labo, mag je die meteen gaan demonstreren bij de lector. Je toont het eindresultaat in de vorm van een werkende omgeving, dus niet enkel aan de hand van een laboverslag. Zorg er in elk geval voor dat de omgeving vooraf klaar staat, zodat je op verzoek specieke zaken kan demonstreren.

Voor enkele labo's is er een tussentijdse deadline opgegeven tijdens het semester:

- Module 1 (CI/CD met Jenkins) moet afgewerkt en getoond zijn ten laatste in W5
- Module 3 (Kubernetes) moet afgewerkt en getoond zijn ten laatste W12

Reguliere studenten die tijdens de contactmomenten geen kans gekregen hebben om het resultaat te tonen aan de lector, kunnen een demo opnemen en via Panopto delen met de lector van jouw klasgroep. Dit moet gebeuren ten laatste op zondagavond van de lesweek waarin de deadline ligt.

De modules 2 (cong management met Ansible) en 4 (monitoring met Prometheus) vormen samen één geïntegreerde opstelling. Deze mag getoond worden tijdens het semester, ten laatste W12 of W13 indien je lector een inhaalsessie organiseert. Eventuele Panoptoopnames van deze opstelling moet ten laatste op woensdag 18 december 2024 ingediend zijn (zodat we voor de start van het winterreces kunnen bepalen of deze voldoende zijn).

Als je alle demo's van de labo's hebt gegeven vóór het winterreces en je haalt voor elk minstens het niveau "bekwaam", dan hoef je niet meer deel te nemen aan het mondelinge evaluatiemoment tijdens de examenperiode.

### **Respecteren van tussentijdse deadlines**

De consequenties van het niet respecteren van deadlines:

M1, M3 ten hoogste één week na de deadline ingediend

- -3/20 per gemiste deadline op het examencijfer
- M1, M3 méér dan één week na de deadline of niet ingediend
	- De opdracht wordt beschouwd als niet gerealiseerd. Je kan niet slagen in de eerste examenperiode.
	- Werk bij voorkeur M2, M4 tijdig af en toon ten laatste op het mondelinge evaluatiemoment in de examenperiode. Labo's die afgewerkt zijn, neem je niet mee naar de tweede examenkans.
- M2, M4 demo niet getoond voor winterreces, of Panopto-opname niet ingediend voor 18/12
	- Geen puntenverlies, je toont deze labo's op het mondelinge evaluatiemoment tijdens de examenperiode.

## **Mondeling evaluatiemoment**

Tijdens de examenperiode is er een mondeling evaluatiemoment voorzien waarop je de laatste labo's (M2 en/of M4) kan tonen die nog niet afgewerkt waren vóór het winterreces.

Dit gaat door via een maximum 20 minuten durend Teams-gesprek (dus online, niet oncampus). Tijdens dit gesprek, demonstreer je je resultaten. Je moet een werkende omgeving kunnen tonen, niet alleen je laboverslag! Om stress en tijdsgebrek tijdens de demo te vermijden, kan je op voorhand een screencast opnemen en deze tijdens het gesprek afspelen en toelichten. Je omgeving moet wel klaar staan zodat je op vraag van de lector "live" zaken kan tonen of vragen beantwoorden.

## **Tweede examenkans**

Wie niet slaagt, krijgt een tweede examenkans in de vorm van een individuele opdracht. De precieze opdracht hangt af van je evaluatie en bestaat concreet uit:

- labo's afwerken van de modules waar je je bekwaamheid nog niet hebt aangetoond, of waar je een hogere score wenst te behalen,
- aangevuld met enkele extra labo-opdrachten die iedereen moet uitvoeren. De nale onderwerpen worden na de bekendmaking van de punten van de eerste examenkans. Je zal de keuze krijgen om een tweetal labo's te maken uit een divers aanbod. Topics die aan bod kunnen komen:
	- Packer, om het aanmaken van VMs te automatiseren (provisioning)
	- OpenTofu als vervanger voor Vagrant (provisioning)
	- Voeg logging toe aan het monitoringsysteem (monitoring, observability)
	- Implementeer M1 met een andere CI/CD tool (software delivery)
	- Helm, een package manager voor Kubernetes (orchestration)
	- Cilium, een Software Dened Networking tool voor Kubernetes (orchestration)
	- Chaos Engineering (orchestration)
	- Draag bij aan een open source project relevant voor het onderwerp van deze cursus

Zoals altijd: schrijf altijd een gedetailleerd laboverslag, waarin je de stappen die je hebt ondernomen om je doel te bereiken, beschrijft. Neem screenshots van tussentijdse en eindresultaten, en hou een cheat sheet bij van belangrijke commando's.

Alle code die nodig is om je opstelling te reproduceren moet in je Github-repository aanwezig zijn.

De opdracht(en) worden gepubliceerd op Chamilo na het bekendmaken van de punten, en enkel aan de studenten die nog geen credit verworven hebben na de eerste examenkans.

Als je vragen hebt over de opdracht, volg dan de richtlijnen in deze studiewijzer (zie Studiebegeleiding) en gebruik meer bepaald het Teams-kanaal. E-mails naar de lector zullen niet worden beantwoord, tenzij het gaat om een persoonlijke vraag. Tijdens het zomerreces mag je niet verwachten dat je antwoord krijgt.

Deadline voor indienen van de opdracht is de eerste dag van de examenperiode, maandag 18 augustus 2025, om 23:59u. Tegen dan moeten al je code en je laboverslagen in je Github-repository staan. Je examencijfer zal gebaseerd zijn op de toestand van je repository op dat moment. Latere commits worden niet in rekening gebracht. Zoals tijdens de eerste examenperiode zal je een online afspraak kunnen maken op een van de dagen die in je examenrooster staan. Het evaluatiemoment duurt max. 30 minuten.