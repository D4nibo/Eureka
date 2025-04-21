19/04/2025 17:09 Infrastructure Automation: inleiding
# **Infrastructure Automation:** **inleiding**
#### HOGENT toegepaste informatica Bert Van Vreckem & Thomas Parmentier 2024-2025

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 1/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
# **Intro**

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 2/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Woensdag 10 maart 2021, 01:31**
#### Inuits on-call team merkt dat enkele VMs “weg” zijn.

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 3/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Dit zijn productiesystemen!**

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 4/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Het lijkt er op dat ze niet** **terugkomen…**

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 5/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Woensdag 10 maart 2021, 03:42**



https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 6/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **De situatie**
#### OVHcloud is een cloudprovider 32 datacenters over 4 continenten o.a. in Straatsburg (SBG)

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 7/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 8/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 9/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 10/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 11/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Je servers zijn dus weg. Wat nu?**

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 12/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Wat was er gebeurd?**
#### Waarschijnlijk een defecte UPS (stroomvoorziening) 3,6M websites, 464K domeinen weg Impact op bedrijven en overheden Geen disaster recovery plan? Vaarwel data! Vaarwel klanten! Vaarwel bedrijf!

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 13/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **De situatie bij Inuits**
#### 130 VMs over 12 servers zijn weg Meeste problemen opgelost door automatische failover naar andere datacenters Enkele “probleemgevallen”…

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 14/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Casus 1**
#### VIP klant, failover faalt Handmatige wijziging DNS record nodig voor de load balancer 1u kwijt: klant had controle over DNS, moesten wijziging zelf doen

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 15/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Casus 2**
#### Klant verspreid over 2 DCs Volledige infrastructuur gereconstrueerd bij andere ISP vóór 9:00 Zonder notificatie zou klant niets gemerkt hebben…

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 16/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Impact op Inuits**
#### **Geen dataverlies!** Meeste problemen opgelost voor aanvang kantooruren

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 17/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Wat is hun “geheim”?**
#### **Infrastructure as Code** Configuration Management Alles is een pipeline! Cloud native Geen eigen HW Multi-cloud, cloud-agnostic High Availability in het design

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 18/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Referenties**

#### Buytaert, K. (2021-06-17)

#### Buytaert, K. (2021-06-17) Help, my . StackConf 2021. **datacenter is on fire!** **https://youtu.be/zDfH0DpHT3s**

#### . StackConf 2021.

#### Rosemain, M. & Satter, R. (2021-03-10) Millions **of websites offline after fire at French** . Reuters **cloud services firm**

#### Rosemain, M. & Satter, R. (2021-03-10)

#### . Reuters **cloud services firm** Witteman, E. (2021-03-15)

#### Witteman, E. (2021-03-15) OVH fire may be **caused by faulty UPS**


https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 19/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
# **Infrastructure Automation**

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 20/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Infrastructure Automation**
#### Gerelateerde termen: Infrastructure as Code GitOps DevOps

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 21/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Levenscyclus van een server**
#### Wat zijn de verschillende fasen in het leven van een server(-VM)?

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 22/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Tooling (1/3)**
#### Tools voor server lifecycle management: Provisioning: lege machine → JEOS Vagrant, Packer, Docker, Terraform/OpenTofu, Pulumi, … JEOS → klaar **Configuration Management:** voor productie Ansible, Puppet, Chef, CFEngine, …

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 23/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Tooling (2/3)**
#### Software Delivery /Release engineering CI/CD: Jenkins, Travis CI, Circle CI, Gitlab CI, Github Actions, … Packaging: rpmbuild, dpkg-deb, fpm Package mgmt: RPM, deb, npm, RubyGems, pip, Helm, Chocolatey, WinGet, … Repository management: Pulp

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 24/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Tooling (3/3)**
#### Orchestration: systemen in productie beheren Ansible, SaltStack, Kubernetes, … **Monitoring:** Traditioneel: Icinga, Nagios, … Time Series DB: Prometheus, collectd, Cacti, … Logging: Grafana Loki, Elastic stack, Splunk, Fluentd, …

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 25/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
# **Studiewijzer**

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 26/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Studiewijzer**
#### Zie Chamilo-cursus voor gedetailleerde info!

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 27/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 28/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Leerdoelen en competenties**
#### Provisioning : Vagrant : **Configuration Management Systems** Ansible Software delivery : CI/CD met Jenkins Orchestration : Kubernetes Monitoring : Prometheus

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 29/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Cursusinhoud**
#### Intro, werkomgeving opzetten M1. Continuous Integration/Delivery M2. Configuration management M3. Container orchestration M4. Monitoring

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 30/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Leermaterialen**
#### Start met het overzicht in de Chamilo-cursus Github: slides lessen labo-opdrachten, Leerpad met links naar Online handleidingen van gebruikte software (e-)Boeken Online cursussen Basiskennis Linux herhalen: linux-training- **hogent**

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 31/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Nodige software**
#### (Mac, Linux: zie studiegids op Chamilo)

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 32/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Software (vervolg)**
#### VSCode: installeer aangeraden plugins (zie studiegids) VirtualBox: Installeer niet 7.1! Extension Pack! Git client: ook Git Bash installeren!

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 33/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Werkvormen**
#### Klassikale instructie en demonstraties Labo-opdrachten

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 34/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Studiebegeleiding**
#### Individuele begeleiding voor labo- opdrachten Stel vragen tijdens de les Buiten de les: algemeen Teams-kanaal Enkel voor persoonlijke vragen: e-mail/Teams chat

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 35/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Evaluatie**
#### **Beoordeling via rubrics** Voor elke opdracht minstens “bekwaam” halen Portfolio : Github repo met broncode en laboverslagen Demo’s : Tijdens het semester: M1, M3 vóór de deadline! On-campus of via Panopto-opname M2, M4 optioneel voor W12 of via Panopto voor 18/12 Examenperiode: M2, M4 via Teams

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 36/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Tweede examenkans**
#### Persoonlijke opdracht, geen begeleiding Niet afgewerkte labo-opdrachten Extra opdrachten (TBD), mogelijke topics: Packer, OpenTofu Cilium, Helm, Chaos Engineering Gitlab CI Grafana Loki Bijdrage open source project

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 37/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Semesterplanning**
#### 1. intro, installatie software M1. Continuous Integration/Delivery with Jenkins 2. (labos) 3. M2. Configuration management with Ansible 4. (labos) 5. (labos) Deadline M1. 6. (labos)

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 38/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Semester schedule**
#### 7. M3. Container Orchestration with Kubernetes 8. (labos) 9. (labos) 10. M4. Monitoring 11. (labos) 12. (labos) Deadline M3. 13. Optioneel: inhaalsessie Wo 18 dec: Deadline Panopto-opnames **(M2, M4)**

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 39/40


-----

19/04/2025 17:09 Infrastructure Automation: inleiding
## **Vragen?**
#### Stel vragen tijdens de contactmomenten Gebruik het Teams-kanaal

https://hogenttin.github.io/infra-slides/00-infra-intro.html#/title-slide 40/40


-----

