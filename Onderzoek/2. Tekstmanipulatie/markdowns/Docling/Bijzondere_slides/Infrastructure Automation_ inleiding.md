## Infrastructure Automation: inleiding

HOGENT toegepaste informatica Bert Van Vreckem &amp; Thomas Parmentier 2024-2025

## Intro

## Woensdag 10 maart 2021, 01:31

on-call team merkt dat enkele VMs 'weg' zijn. Inuits

## Dit zijn productiesystemen!

## Het lijkt er op dat ze niet terugkomen…

## Woensdag 10 maart 2021, 03:42

We have a major incident on SBG2. The fire declared in the building. Firefighters were immediately on the scene but could not control the fire in SBG2. The whole site has been isolated which impacts all services in SGB1-4. We recommend to activate your Disaster Recovery Plan.

March 10,

- Octave Klaba (@olesovhcom) 2021

## De situatie

- is een cloudprovider OVHcloud
- 32 datacenters over 4 continenten
- o.a. in Straatsburg (SBG)

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Je servers zijn dus weg. Wat nu?

<!-- image -->

## Wat was er gebeurd?

- Waarschijnlijk een defecte UPS (stroomvoorziening)
- 3,6M websites, 464K domeinen weg
- Impact op bedrijven en overheden
- Geen disaster recovery plan? Vaarwel data! Vaarwel klanten! Vaarwel bedrijf!

## De situatie bij Inuits

- 130 VMs over 12 servers zijn weg
- Meeste problemen opgelost door automatische failover naar andere datacenters
- Enkele 'probleemgevallen'…

## Casus 1

- VIP klant, failover faalt
- Handmatige wijziging DNS record nodig voor de load balancer
- 1u kwijt: klant had controle over DNS, moesten wijziging zelf doen

## Casus 2

- Klant verspreid over 2 DCs
- Volledige infrastructuur gereconstrueerd bij andere ISP vóór 9:00
- Zonder notificatie zou klant niets gemerkt hebben…

## Impact op Inuits

## Geen dataverlies!

- Meeste problemen opgelost voor aanvang kantooruren

## Wat is hun 'geheim'?

## Infrastructure as Code

- Configuration Management
- Alles is een pipeline!
- Cloud native
- Geen eigen HW
- Multi-cloud, cloud-agnostic
- High Availability in het design

## Referenties

- Buytaert, K. (2021-06-17) . StackConf 2021. Help, my datacenter is on fire! https://youtu.be/zDfH0DpHT3s
- Rosemain, M. &amp; Satter, R. (2021-03-10) . Reuters Millions of websites offline after fire at French cloud services firm
- Witteman, E. (2021-03-15) OVH fire may be caused by faulty UPS

## Infrastructure Automation

## Infrastructure Automation

Gerelateerde termen:

- Infrastructure as Code
- GitOps
- DevOps

## Levenscyclus van een server

Wat zijn de verschillende fasen in het leven van een server(-VM)?

## Tooling (1/3)

Tools voor server lifecycle management:

- Provisioning: lege machine → JEOS
- Vagrant, Packer, Docker, Terraform/OpenTofu, Pulumi, …
- Configuration Management: JEOS → klaar voor productie
- Ansible, Puppet, Chef, CFEngine, …

## Tooling (2/3)

- Software Delivery /Release engineering
- CI/CD: Jenkins, Travis CI, Circle CI, Gitlab CI, Github Actions, …
- Packaging: rpmbuild, dpkg-deb, fpm
- Package mgmt: RPM, deb, npm, RubyGems, pip, Helm, Chocolatey, WinGet, …
- Repository management: Pulp

## Tooling (3/3)

- Orchestration: systemen in productie beheren
- Ansible, SaltStack, Kubernetes, …

## Monitoring:

- Traditioneel: Icinga, Nagios, …
- Time Series DB: Prometheus, collectd, Cacti, …
- Logging: Grafana Loki, Elastic stack, Splunk, Fluentd, …

## Studiewijzer

## Studiewijzer

Zie Chamilo-cursus voor gedetailleerde info!

## Leerdoelen en competenties

- Provisioning : Vagrant
- Configuration Management Systems Ansible
- Software delivery : CI/CD met Jenkins
- Orchestration : Kubernetes
- Monitoring
- : Prometheus
- :

## Cursusinhoud

- Intro, werkomgeving opzetten
- M1. Continuous Integration/Delivery
- M2. Configuration management
- M3. Container orchestration
- M4. Monitoring

## Leermaterialen

- Start met het overzicht in de Chamilo-cursus
- Github: , slides lessen labo-opdrachten
- Leerpad met links naar
- Online handleidingen van gebruikte software
- (e-)Boeken
- Online cursussen
- Basiskennis Linux herhalen: linux-traininghogent

## Nodige software

```
PS> winget install Git.Git PS> winget install Microsoft.VisualStudioCode PS> winget install Oracle.Virtualbox --version 7.0.20 PS> winget install Hashicorp.Vagrant
```

(Mac, Linux: zie studiegids op Chamilo)

## Software (vervolg)

- VSCode: installeer aangeraden plugins (zie studiegids)
- VirtualBox:
- Installeer niet 7.1!
- Extension Pack!
- Git client: ook Git Bash installeren!

## Werkvormen

- Klassikale instructie en demonstraties
- Labo-opdrachten

## Studiebegeleiding

- Individuele begeleiding voor laboopdrachten
- Stel vragen tijdens de les
- Buiten de les: algemeen Teams-kanaal
- Enkel voor persoonlijke vragen: e-mail/Teams chat

## Evaluatie

## Beoordeling via rubrics

- Voor elke opdracht minstens 'bekwaam' halen

## Portfolio :

- Github repo met broncode en laboverslagen

## Demo's :

- Tijdens het semester:
- M1, M3 vóór de deadline!
- On-campus of via Panopto-opname
- M2, M4 optioneel voor W12 of via Panopto voor 18/12
- Examenperiode:
- M2, M4 via Teams

## Tweede examenkans

Persoonlijke opdracht, geen begeleiding

- Niet afgewerkte labo-opdrachten
- Extra opdrachten (TBD), mogelijke topics:
- Packer, OpenTofu
- Cilium, Helm, Chaos Engineering
- Gitlab CI
- Grafana Loki
- Bijdrage open source project

## Semesterplanning

- 1. intro, installatie software M1. Continuous Integration/Delivery with Jenkins
- 2. (labos)
- 3. M2. Configuration management with Ansible
- 4. (labos)
- 5. (labos) Deadline M1.
- 6. (labos)

## Semester schedule

- 7. M3. Container Orchestration with Kubernetes
- 8. (labos)
- 9. (labos)
- 10. M4. Monitoring
- 11. (labos)
- 12. (labos) Deadline M3.

13. Optioneel: inhaalsessie

Wo 18 dec:

Deadline Panopto-opnames

(M2, M4)

## Vragen?

- Stel vragen tijdens de contactmomenten
- Gebruik het Teams-kanaal