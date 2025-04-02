"""Test data"""

import pytest


@pytest.fixture
def transcribed_poem_lines():
    """2132_Forord_no-nb_digibok_2006082400076"""
    lines = [
        [
            "D AX0 R",
            "V AA1 R",
            "UU2 F R EH3 D",
            "IH0",
            "L AH2 N AX0",
            "P OA3",
            "T OAH1 R V AX0",
            "S T OO1 D",
        ],
        [
            "EE1 N",
            "V AH2 N D R AX0 N AX0",
            "S V EH1 N",
            "M EE1",
            "S II1 N",
            "KJ OE2 P M AH0 N S B OO3 D",
        ],
        [
            "AH0 F",
            "SJ IH2 N NX0 AX0",
            "S M YH3 K AX0 R",
            "L OA1",
            "D IH1 S K AX0 N",
            "F UH2 L",
        ],
        [
            "D AX0 R",
            "V AA1 R",
            "B AE2 L T AX0 R",
            "AH0 F",
            "S IH2 L K AX0",
            "OA1",
            "R IH2 NG AX0 R",
            "AH0 F",
            "G UH2 L",
        ],
    ]
    return lines


@pytest.fixture
def orthographic_poem_lines():
    """2132_Forord_no-nb_digibok_2006082400076"""
    lines = [
        ["Der", "var", "Ufred", "i", "Landet", "Paa", "Torvet", "stod"],
        ["En", "vandrende", "Svend", "med", "sin", "Kjøbmandsbod"],
        ["Af", "skinnende", "Smykker", "laa", "Disken", "fuld"],
        ["Der", "var", "Bælter", "af", "Silke", "og", "Ringer", "af", "Guld"],
    ]
    return lines


@pytest.fixture
def example_poem_landsmaal():
    """Poem ID: 2873_Arne_Garborg_no-nb_digibok_2014073108102"""
    return """Kvass som kniv
i daudkjøt flengjande.
Sanningstyrst
mot ljoset trengjande.


Varm av elsk,
som granskog drøymande.
Frisk som foss
Or berget strøymande.


Nyreist Norig
eldfullt byggjande.
Hovding hæv
um tufti tryggjande!
"""


@pytest.fixture
def example_poem_riksmaal():
    """Poem ID: 766_Kjærligheden_no-nb_digibok_2014110308161"""
    return """Kjærligheden ‒ kjendte du dens glød?
Ren som guld fra Herren selv den flød.
Ædelt, høit og helligt som vor Gud
Er det lovens allerstørste bud.


Kjærligheden ‒ kjendte du dens magt,
Sterkere end døds og helveds pakt?
Mange vande kan ei slukke ud
Kjærligheden, som udgår fra Gud.


Kjærligheden ‒ kjendte du dens værd,
Virksomt, ja langt mer end noget sverd?
Al den ildske, som i verden er,
Overvindes, når den kommer nær.


Kjærligheden ‒ kjendte du dens ånd,
Klippesterke, kjærlighedens bånd?
Større dyd på jord ei nævnes kan,
End den ædle kjærlighedens brand!
"""


@pytest.fixture
def example_poem_danish():
    """Poem ID: 3107_EngelskeSocialister_no-nb_digibok_2015102908059
    Only the 3 first stanzas
    """
    return """Henover Byens Tage glide
de sidste Smil, de hendøende Rester
af Dagen og Solen. I Strømninger stride
vælter sig Flodens mudrede Vande,
og som indbuden Gæst til det smudsige Leje,
fra Havets, fra Nordsøens vaade Veje,
sænker sig Taagen over Byen, over Strømmen,
saa kommer Natten, Døden eller Drømmen!


I Læ for Vinden, i Ly for Taagen,
omkring et Kulbaals ulmende Gløder ‒
rapsede Varer derhenne fra Krogen,
hvor Købmanden losser de drægtige Skuder, ‒
sidder et Selskab. Sod paa Skjorten,
knudrede Arme, en tretten, fjorten
Stykker af dem, der lossede Skuden:
Angelsachsernes Blod ruller under Huden.


De mumler dæmpet og suger paa Piben,
Øllet gaar om i de klinkede Kander,
der er Noget paafærde, man vil ud af Kniben,
man har Noget paa Hjerte, vil Nogen paa Livet;
men skønt Armen dirrer, og Pulsen banker,
mangler man Ord for de mange Tanker;
der er Galskab nok, men System er der ikke.
Da rejser en Mand sig med funklende Blikke.
"""


@pytest.fixture
def poem_with_anaphore():
    """Poem ID: 1924_Jeg_ser_no-nb_digibok_2009010803011"""

    return """Jeg ser.

Jeg ser paa den hvide himmel,
jeg ser paa de graablaa skyer,
jeg ser paa den blodige sol.

Dette er altsaa verden.
Dette er altsaa klodernes hjem.

En regndraabe!

Jeg ser paa de høie huse,
jeg ser paa de tusende vinduer,
jeg ser paa det fjerne kirketaarn.

Dette er altsaa jorden.
Dette er altsaa menneskenes hjem.

De graablaa skyer samler sig. Solen blev borte.

Jeg ser paa de velklædte herrer,
jeg ser paa de smilende damer,
jeg ser paa de ludende heste.

Hvor de graablaa skyer blir tunge.

Jeg ser, jeg ser...
Jeg er vist kommet paa en feil klode!
Her er saa underligt...
"""


@pytest.fixture
def poem_with_alliteration():
    """Poem ID: 2735_Sirius_som_Séer_no-nb_digibok_2009010803031"""
    return """Stjerneklare Septembernat
Sees Sirius,
Sydhimlens smukkeste
Stjerne,
Solens skjønneste Søster,
Svæve saa stille,
Straale saa smukt,
Skue sørgmodigt
Slægternes Strid.
Sine samlede Syner
Sender Stjernen Sirius
Sine store Slægtninge:
Solen, Skorpionen,
Stolte, svømmende Svane,
Sydkorset, Saturn,
Som straalende Stjerneskud.
Sirius ser saameget!
Ser Sagas skyhøie Sæde,
‒ Store Skagastølstind ‒
Som sydfor Snehætten staar.
Saga speidende sidder
Ser ‒ samler ‒ skriver.
Samler, som Snorre Sturleson,
Samler, som Seeren Saxo,
Samler stortænkte Skrifter,
‒ Stengamle, støvede Skrifter
Saavelsom senest skrevne –
Skaldene, som siger Sandheden smukkest,
Sender Saga sit stolteste Smil.
Saalangt, som Samfund stiftes,
Ser Saga  samler  skriver.
Saaledes ser Saga:
Store Stater
Svinge sit skarpe Sværd,
Sønderlemme Smaastater,
Snigmyrde Smaafolk,
Som sturende sidder.
Smaafolk, som saares,
Strider, søger sig skjærme
Saavidt Smaafolk skjønner,
Saalangt Synet strækker.
Store Staters Styggedom
Skabte Socialisternes Stræv.
Sligt ser Saga ‒ sukker ‒ skriver.
Stundimellem samler Saga Slægtregistre,
Som senere Slægter ser.
Sommetider Stormagter skjændes,
Som sletikke Saga ser:
Saaledes saa Sirius
Søndenvinden skamskjelde Snedronningen
Sidstleden syvende September.
Søndenvinden sagde spydigt:
“Snedronningen sidder saa stille,
Spiser Spitsbergens skidne Sne,
Skjønt Solen skinner saa smukt
Sydover solrigs Septemberdag.
Seil sydover, skjønne Snedronning!
Se Spaniens smukke Stæder,
Se Spaniens storladne Sæder,
Som sømmer sig stolte Snedronning.
Spis svulmende Sydfrugter,
Smag Spaniens søde Safter,
Sligt skal styrke Segnende,
Skjærpe Svages slappe Smag.
Saadan Stillesidden
Samt stadig Surmulen
Skader sarte Skjønhed.”
“Seil selv sydover, satiriske,
Spottende, springfyragtige Spasmager,”
Svarer Snedronningen stolt,
Saa slipper Snedronningen sligt
Slidder, Sladder, Sladder!
Spitsbergens skinnende Sale
Samt sølvklare Sneboller
Smager styrkende  sundt.
Søndenvinden skal sagtens
Slikke Sydens Stæv,
Søke stikkende Sol.”
“Stive Snerpe”! sagde Søndenvinden.
Sjofelist!
Slu, snedige Slubbert”!
Svarte Snedronningen sint.
Snip, Snap, Snude,
Saa slutter Snedronningens Sagn.


Sceneriet skifter,
Sirius smiler,
Sender Søster Skorpionen
Synerne som Stjerneskud.
Særligt saadanne Syner:
Storthingsmænd sludrer sværtlænge,
Skraber sig Skillinger sammen,
Sløser Statens Sølvmynt,
Sætter Skatten svært stor.
“Sir Søren” staar saa skjændende,
Ser Statskassens Skatte svinde,
Siger sine Samarbeidere Skoser,
Som stelte Skjødebarnet slig.
Sverdrup senior siger stadigt:
“Se saa skal Skabet staa.”
Sognepræst Sverdrup svinger Svøben,
Snerter stygt sine Sidemænd,
Sætter sig selv saa stor.
“Snilde som Slanger”
Staar Schweigaard, Stang;
Stang slaar Stortrommen,
Schweigaard stemmer sin Strængeleg.
Smukke Samspil
Smelter Sjæle,
Saa Stivsindet svinder,
Som Sol smelter Sne.
Slagfærdig staar Storbladsmand Schøien.
Steen ‒ Stavangers Skolemand –
Siger snart saa  snart saa.
Somme sidder svært selvgode,
Soelberg snakker sletikke.
Storpralende Storbønder sidder
Somoftest søvnige  stumme.
Stemmeretten skrinlagdes skammeligt,
‒ Samtlige Stormænds største Streg.
Saaledes Storthingsmænd saares,
Som sliter saa surt,
Søndag som Søgnedag.
Skjæbnerne skifter  Sirius ser
Storthingsmænd stige,
Sæge sig større Stilling,
Sikre sig Statsraadstaburetten,
Staa snart som Statens
Største Styrere,
Styre Statsskibet saa som saa.
Stjernen Sirius smiler skjælmsk,
Sender sine Stjerneskud,
Saasnart svenskefjæskende Statsraader
Steller, stuller, styrer snodigt:
Se saaledes salig Stangs Styretid,
Senere Selmer, Schweigaard,
Stang, Sverdruperne, samt
Saakaldet stumme Stang,
Jom styrtedes sidst.
Skulde saamange store Stænger
‒ Store Slægters store Sønner –
Staa svaiende?
Svigte sit Statskald?
Saagodtsom sælge Staten?
Smigre Svenskerne?
Staa som Statsforrædere?
Sladder! Stort Sluddær!
“Sletingen støtter som store Stænger.”
Siger Storbladene smukt som sandt.
“Skidt san! Slige slingrende Støtter!”
Svarer Smudsbladene spidsfindig.
Steen!
Store Steen skal sandelig staa,
Som Statens solideste Støtte!”
Smudsbladene skreg selvfølgelig:
“Sten! Sten! Sten!”
Sædt smilede Skolemanden Steen,
Sendte Stavangerne Slængkys,
Beilede, skulde snart Storbyen se,
Skulde snart Slægten syne
Stordaad, som sjelden spurgtes.
Snart som Storbyens Stormand
Stod samme Skolemand,
Samlede sit Skrækministerium,
Som skal sætte Svensken Stenen,
‒ Sletikke Stangen –
Sletikke staa som svaiende Stang.
Skrækslagne saa Storbladene
Steen samle slette Subjekter,
Som skal Staten styre.
‒ Slette Subjekters store Synder
Samled Storbladene samvittighedsfuldt,
Saa Slægten skulde se
Statsministerens store Skjævsyn,
Som satte slige sjofle Stakkarer
Som Statsraader.
“Skurkagtigt Svinepak!”
“Sørgeligt Satansværk!”
Sukked Storbladene saart.
Sexsogsyvti slige Skjældsord
Skjæmte stadigt Spalterne.
Slige stygge Skriverier
Sees stadig som
Storpartiets største Styrke.
Samtidig skildred Smaabladene
Statsministeriet Stang.
Strax sagde Storbladene:
“Smudsbladene skumler,
Skriver stygt, samvittighedsløst.
Siger saamange Storløgne,
Som skal skræmme svage Sjæle.
Smudspressen sparker saa skrækkeligt
Storbladenes Stormænd,
Søndertrampes, sønderknuses, sønderrives
Skulde sligt Skadedyr,
Søndenvinden Stumperne sprede,
Saa Styggeriet svandt
Som Søens salte Skum.”
Saadanne stygge Stiklerier
Storbladene stadig skriver,
Siger Smaabladene saameget skarpt,
Som skal Smaafolk skræmme.
Smaabladene, stakkar,
Svarer sjelden,
Skriver skaansomt,
Saarer sletikke.
Sandelig stor Synd,
Smaabladene skal
Skamskjændes slig!


Som sagt,
Statsskibet styres saa som saa:
Somme ser Stormen
Skuden slænge,
Søuhyrer svære
Skuden sluge,
Søen sprøite, skumme,
Saa Skuden synkefærdig synes.
Sørgelige Spaadomme
Spørges sommetider.
Saaledes siges som sikkert:
Storrussen skal snart
Sværdet svinge,
Sønderlemme,
Sønderhugge
Statsskibet, som styres saa slet.
Splitte Slægter,
Snigmyrde, stjæle
Stort som Smaat;
Sende Størsteparten Søveien,
Som Storruslands selvtagne Skat.
Spydige Slængord
Slaar stakkars Statsraader
Som Stenkast.
Skamfuld staar Statsraadflokken.
Selvforskyldte Svøbeslag
Smager sletikke.
Somme synes sandelig
Skuden styres smukt,
Synes Statsraader skalter,
Slig som sig sømmer
Selvstændigt Styre.
(“Se Skandalpressen”
Siger Storbladene.)
Sandsynligvis sker snart som spaaet:
Statsraader skynder sig
Sin Statsraadtitel sælge,
Sæge sin simple Stand,
Sin svundne Stilling;
Staar snart som Sognepræster,
Snart som Skolemænd,
Snart som Skrivere,
Somme som Storbønder
Skjuler sig ‒ svinder
Som sjælløse Skygger.
Skulde synes,
Slige stakkars svundne Storheder
Skulde skræmme,
Saa Slægten senerehen
Stadigt saa sit stolteste Syn, –
Saa Storbladsmænd
Som Statens Styrere!
Storhjertede Storbladsmænd,
Som sidder stivryggede,
Smukke, staute, solide,
Slig som sig sømmer
Stockholmsfarere, samt
Slottets som Stiftsgaardens Størrelser.
“Saadant ske snarest!”
Sukker Storbladene.
Statsraadhuden synes sandelig stenhaard!
Sirius ser Striden!


Sognepræsterne synes
Sognebørn sparer saameget:
“Sænder saa sjelden Smør,
Bauer, samt større Steger.
Sjælesørgere skal skattes,
Sendes Stymperes sidste
Styver.”
Saaledes snakker Sorte
kjolerne
Sagtelig sigimellem.
Sognefolk skulde sig
skamme !
Sværte sine Sjælehyrder slig!
Sirius ser stadigt skiftende Syner:
Ser Skuespillere sværtmange Steder
Spille skrækkelig slet,
Saa skuelystne Skarer
Sletintet skjønner.
Saaledes spiller sletikke
Schrøders Skuespillere,
Som studerer sine Sager;
Spiller selvfølgelig smukt
Saamangen Storaands Syner,
Saamange storslagne Sørgespil.
Samtidig sløifer
Schrøders Scene
Skurrile stykker.
Saaledes siger Schrøder:
“Saavel Storbjørnen som
Skribenten, som skrev
“Samfundets Støtter”,
Skal sletikke se
Sine samlede Skuespil;
Sligt Snaus
Skal sandelig spilles sjelden.
Scenen skal samle
Smaa skjælmske Skovaber,
Som skaber sig!
Sligt styrker Skuespilsansen,
Styrker Samspillet,
Skaffer saamangen sund Skoggerlatter.”


Storbjørnen skjæmmer sig storligt,
Stakkar!
Skifter saaofte Sind:
Staar snart som Slingringsmand,
Slænger snart som Stormhanen,
Staar stundom stiv, stram, strunk,
Skravler stundom som Spaakjærring,
Skulde stille, sympathetisk, standhaftig
Som Skjeidkampen staa,
Saa skulde Skalden stille
Slægtens store Sjælevunde,
Stills saamange skjulte Savn.
Snart synger Skalden
Smukke Sange,
Snart sender Skalden
Særsynte Skrifter,
Som sætter Skræk,
Skildrer Samfundssynderne stærkt,
Straffer strængt.
Snart som Skribent,
Snart som Stortaler
Skildrer Storbjørnen selvgod sin Samtid.
Søndagsfreden skildres smukt,
Søgnedagsstriden skildres sandt,
Storpolitisk Sludder skrives somoftest, ‒
Svaier saaledes selv som Siv.
Smaastæders Skjødesynd, Sladder,
Skaaner sletingen Skjønaand.
Sandheden skal siges:
Skjønneste Syn Sirius saa –
Slægtskjærligheden
Sætter Storbjørnen størst:
Steller store Søstre smukt
Sine smaa svage Søskende,
Sender Sirius strax
Særegne Stjerneskud,
Som skildrer Sydkorset
Slige Søskendes Samliv.
Saafremt store Sønner
Skaffer sin Slægt Sorg,
Skjuler Sirius sig strax.
Som stor, sort Stenmur
Stænger svære Skymasser
Samtlige Stjerners Skjønhed,
Saa slige slemme Sønner
Staar som stærblinde,
Ser ‒ sort – sort ‒ sort.
Strængt straffer Skjæbnens Styrer
Slægtens skammeligste Synd,
Sender saaledes Sygeleie,
Sværtmange slemme Sygdomme,
Store Smerter, Sult,
Sorger, saamange Slags Savn,
Som slider, sønderriver,
Skjærer slemme Saar,
Som svulmer, svider.
Sommetider sendes Snedrev,
Storm, Skypumper, Stormflod,
Som seigpiner samtlige,
Saa sidste Søvn synes sød.
Sligt sees stadigt,
Skjønt Sekler svandt
Siden sidste store Syndflod.
Syndfloden, som skyllede,
Sopte ‒ steg ‒ steg ‒ steg –
Saaat svaiende smaa Sivplanter
Saavelsom skyhøie Snefjelde skjultes.
Største Sømand, Sirius saa,
Sparedes, samt Sømandens
Skyldfri Sønner.
Sømanden ‒ senere Slægters
Stamfader ‒ sparedes,
Samt Sømandens skyldfri Slægt.
Sirius svæver saa stille,
Straaler saa smukt,
Skuer sørgmodigt
Slægternes Strid,
Skjuler sig somoftest,
Saasnart Skjæbnens Styrer
Sender slige svære Straffedomme.
Storbjørnen ser som Sirius!
Som Sirius sender sine Stjerneskud,
Saaledes skildrer Storbjørnen
Samtiden sine Syner.
Syndens sanseberusede Slavinder
Ser saare sjelden
Solen skinne,
Stjerner straale ‒ smile.
Saadanne syndige Stakler
Staar stærblinde,
Ser som Sønnerne
Sort ‒ Sort ‒ Sort.
Standhaftighed!
Slutter Spindesiden sig sammen,
Skal snart Skandalvæsenet svinde,
Saa Staklerne staar seende,
Som skikkelige Samfundslemmer.


Skjønhedssansen staar svært stille:
Saaledes smukkeste Statue
Skildres som stygt Skabilken,
Stemningsfulde Studier slænges
Som styggeste Skilderi.
Skjønliteraturen staar saa som saa:
Somme samler Skandalhistorier,
Sætter sammen – skriver ‒
Sælger sligt som Skjønliteratur.
Skeptikeren skriver sine Synsmaader,
Sofisten sine Slutninger,
Stoikeren sine strænge Sædelighedskrav,
‒ Samtlige synes, sit Smøreri
Staar som sandeste Skjønliteratur.
Saare sjelden sees Skjønliteraturen
Samle Stoffet smukt,
Skjærpe Synet,
Skjænke Sjælen Skjønhedsindtryk,
Som sent svinder.
Studerte Smaaskribenterne
Sappho,
S-Zola,
Shakespeare,
Schiller,
Schandorph,
Strindberg,
Sivle,
Saaes sandelig sjeldnere
Saamange slette Skrifter.
Sidstnævnte syv Skalde
Sendte  som sender ‒
Skrifter, som sent skal
Smuldres som Støv.
Saadanne Skrifter,
Som samtlige sendte,
Skildrer Sjælelivet smukt,
Skildrer Sorgerne sandt,
Skildrer Striden selvstændigt,
Skildrer Seieren straalende,
Skilsmissesager sympathetisk,
Situationer saftigt;
Stemningsfuldt skildres
Salige Stunder.
Stilen storslagen skjøn.


Satirens Svøbe
Skulde sletikke skaane
Skrivelystne Stymperel!
Saadant ser Sirius.
Sommetider ser Sirius
Stakkels smaa Studenter,
Som sidder sultne,
Studerer sig syge.
Slige stakkels Studenter
Studerer særligt Stjernevidenskaben,
Ser Solnedgangen,
Sidder studsende,
Spørger sig selv saaledes:
Sodiakallyset?
So ‒ di ‒ a ‒ kal ‒ ly ‒ set ‒?
Skjønner sletikke sligt!
Som stille Snefald
Sees Sodiakallyset,
Saasnart Solen sig skjuler.
“Synes”, siger Studenten,
“Synes, Sodiakallyset
Staar som Stjernen Saturns
Skjønne Straalering?
Sikkert selvsamme Stof!”
Siger Studenten sjæleglad.
Studenten staar stille,
Ser snart Saturn,
Snart Sodiakallyset,
Sammenligner,
Smiler selvtilfreds.
Sluttelig søger Studenten
Stivfrossen sin Seng,
Sover snart sødelig.
Siriusstraalerne skiftede smukt.
Studentens søde Smaasnak
Sendte Sirius strax
Sin stolte Søster Svanen.
Svanen snaddrede selsomt,
Smaalo, svømmede sydligt:
Søde Søvn svinder snart,
Stenhaarde Søvn sig sænker,
Skaffer Studenten slemme Syner.
Stakkels Student spreller,
Snorker skrækkeligt,
Snakker, slaar, spender
Sin Sengkammerat,
Skriger stundimellem saa:
“Spæktralanalyse!
Spektroskop!
Se Solspektret, Schiaparelli!
Solpletter, Solfakler, Sol, Sol!”
“Stop!” skraaler Sengkammeraten,
“Slig sindssvag Snak
Skræmmer Søster Stine,
Som sidder selvanden,
Syr Sømandsdragt samt
Særker sex,
Som skal sendes Statsraadinden,
Saasnart Stjernehæren svinder,
Solen sine Straaler sender.
Skræmmer saadan Støi
Stakkels Søster Stine,
Syes Svømmedragten sent,
Som skal sendes senest sex.
Saasnart Slaguhret slaar syv,
Seiler Statsraadinden,
Beiler sydtil Sandefjord,
Søgende sin Sundhed;
Søbadet skal skaffe
Sundheden, som svandt.
Skjønne Statsraadinde!
Smukke, slanke Statsraadinde
Skal sletikke staa
Som Susanna splitternøgen!”
Sovende svarer Studenten:
“Sludder!
Splitternøgen Statsraadinde!
Svømmedragt, Særk!
Sludder!
Solfakkel, Sol, Sol!”


Stadig ser Sirius skiftende
Syner:
Ser saameget snurrigt
‒ Skjønt som stygt –
Ser Sladresøstre
Støiende sidde sammen,
Skravle, skrige, skryte,
skraale,
Sværte stygt sine
Søskende.
Samtidig strikker Søstrene,
Som sidder saaledes
sammen,
Søde smaabitte Strømper,
Som sorte Sulubørn slider.
Samtidig syr Søstrene,
Som sladrer saaledes sammen,
Store, svære Skjorter,
Som stormvante Sømænd slider.
Somme sætter Sulumissionen,
Somme sætter Sømandsmissionen,
Somme sætter Santalmissionen
Som Slægtens største Sag.
Sirius ser sligt, som sjelden sker,
Saavelsom Smaatterier,
Ser Smaatterier
Saavelsom Storstadsherligheder.
Ser saaledes Sminken
Skjule store Skrøbeligheder,
Baa selv stygge Skygger
Sees som Skjønheder.
Ser Snørlivet, som skaber
Slanke Sylfider,
Smækkre Sylfider,
Som slangeagtigt snor sin
Smukke Svanehals.
Sirius ser saameget:
Ber Slagterne slaa
Studene skrækkelig stygt,
Synge slibrige Sange,
Som skræmmer Smaajenterne slemt.
Skræddersvendene sender
Sin stygge, sjuskede Søm,
Skomagerdrengene stjæler
Svendenes Saalelæder.
Smed slog Satansnødden
Som Sopelimspinden stængte,
Saa Smietaget strøg;
Storslæggas Smaastumper
Saaes senere spredte
Søndenfor Skudesnæs.
Stupiger, Sypiger, Sergeanter
Slaaes sluttelig sammen,
Seiler saa sin Sø.
“Særlaget” samler saadanne smukt.
Skyhøit sætter somme ‒
“Særlagets” Stifter,
Somme snakker stygt  syndigt,
Siger:
“Særlagets” Stifter søger Strid,
Sætter Splid,
Snakker saameget Sludder,
Sløver selvfølgelig
Svagsinte Smaapigers
Sunde Sands.
Stifteren skulde sandfærdig sendes
Saalangt, som Sibiriens Sneørkner sig
Straffende strækker.”


Septembermaanederne
Skaffer somoftest
Sirius snurrige Syner:
Saaledes ser Sirius
Skolefolk sidde sammen,
Studere, stirre, sige som saa:
“Straffes skal Syndere smaa,
Saa slipper Samfundet senere
Saamange store Syndere,
Som sælger sin Sjæl,
Soner sin svære Straf.”
“Spot som Skam slig Straffelyst!”
Svarer Sagfører Sørensens,
“Smaabørn skal sletikke straffes,
Sletikke slaaes!”
Sagfører Sørensens samlede, skrev
Skrækkelige Sladrehistorier sammen,
Som skulde Skolefolk syne
Sin store Skyld,
Som slog slig søde smaa Stakler,
Saa Spanskrøret sønder sprang.
Somme smaa Stakler sloges syge,
Somme smaa Stakler spottedes saart.
“Sligt Skolevæsen skal stoppes,”
Skrev Sørensens stadig strængt.
“Særensens Skriverier skal stoppes!”
Skreg samlede Skolelærerstand,
“Sagsøges skal sandelig
Sagførerparret!”
Som sagt saa skede.
(Se Sørensens Sag,
Som sluttede sexogtyvende September.)
Somme syntes Sørensens Sag stod slet,
Syntes Sørensens skulde
Satisficere
Samtlige Skolelærere.
Skolelærerne saa
Stor Sympathi,
Skjønt Sørensens Sag seirede;
Somme sagde saagar:
“Schjødt stelte sandelig Sagen slig.
Som Schjødt selv syntes,
Skjældte, smældte,
Spurgte spidsfindigt,
Sendte snartænkt
Spydige Snerter,
Saa Staklerne stode
Sindsforvirrede,
Skamfulde, stumme.
Selvfølgelig staar Sørensens
Skyldfri, straffri,
Seiersstolte.”
Saaledes skrev Storbladene.
Smaabladene studerte stadigt
Sagens sande Sammenhæng,
Samlede store Sandheder,
‒ Saa Skyggesiderne ‒
Summerte sluttelig saa:
“Stor Sag –
Stor Sensation!
Sørensens stred storhjertet
Simple Smaafolks Sag.
Sagkyndig seet
Skulde Sørensens seire.”
Schjødt smilte sagtmodig,
Sagde stilfærdig:
“Styg, smaalig Snak
Skader sletikke
Stærke Skuldre.”
Se, slig Strid ser Sirius.



Sommetider ser Sirius
Saameget smaat, snevert,
Ser saaledes syv smale
Spalter,
Som sluger saamegen
Smaamynt.
Snille Schibsted! Sæt
Spalter sex!
Snille Schibsted! Sløif
syvende Spalte!
Sæt Spalterne slig,
Som Spalterne stod
Sidste September.
Smilende ser Sirius
Somoftest saameget smukt:
Ser Solstraaler spille,
Ser Snefaanner svinde,
Ser Smaablomster spire,
Skyde, sætte Stængel,
Ser Sommerfugle slikke
Sol, som Stængelens Stæv,
Ser Skovalfer sværve,
Skovsangerne smaakviddre,
Søerne sødelig smile,
Skov som Skrænter speile,
Stormen Skyerne sprede,
Solstreif skyndsomst stille
Skabningens skjulte Suk.
Støvøiet synes, sligt staar smukt,
Siriusøiet samler saadant smukkere.
Sommetider ser Sirius
Selskaber slutte sig sammen,
Spadsere store Strækninger ‒
Søgende sjeldne smukke Steder,
Som skal sees, studeres.
Stien slynger sig
Stærkt stigende.
Steilt Skrænterne sænker sig.
Saasnart Stenheller sees,
Søger samtlige Siddeplads.
Spiselige Sager serveres,
Snapser supes,
‒ Somme super Sherry ‒
Somme spiser,
Somme spaser,
Somme skjændes,
Somme slaaes.
Støien skræmte
Smaafuglene, stakkar,
Som sad stille syngende,
Slog sine søde Smaatriller,
Som stilned smaaningom.
Somme sidder stille,
Skriver Stedet smukke Sange;
Somme stiller Staffeliet,
Smører Studier sammen.
Sortkridtet skitserer
Snefjeldet som Søen,
Snebræen som Skoven,
Snevandet som samler sig,
Styrter, suser,
Slynger sig,
Skaber store Stryg,
Som skyndsomst søger
Sørfjorden, smilende, speilblank.
Se saaledes:
Stendalsfossen.
Sjelden smuk stod Solopgangen,
Solnedgangen smukkere.
Sidste Straale
Sendte Stedet
Slumrekys.
Septemberkvælden
Sænkede sit sorte Slør.
Selskabet sig skynder
Søge Stien sydover.
Somme snakked,
Somme sang,
Somme sagde:
“Se Stjernerne!”
“Se Sirius!
‒ Storhunden ‒
Straalende smuk,
Svæver saa stille,
Ser Slægternes Strid.”
Stendalsfossens svindende Sus
Samlede Sindene,
Sendte som Sirius
Stemningsfuld Stilhed.
Siriussynerne skifter stadigt:
Saaledes ser Sirius
Sygdom slide
Syndere, som sukke,
Ser Sygesøstre sidde stille,
Synge smukke Salmer,
Ser Synderes Sjæle
Salige svæve,
Skinne som Sole,
Straale som Stjerner.
Sandheden seirende staar,
Synd som Sorger svundet,
Striden sødelig stilnet,
Skilte sammenføiet.
Smilende, skiftende Sted
Ser Sirius saameget smukt,
Sender Sydkorset Synerne
Som straalende Stjerneskud.

Slut.
"""
