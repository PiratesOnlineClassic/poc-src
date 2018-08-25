from pirates.piratesbase import PLocalizer
from pirates.quest import QuestDB
from pirates.quest.QuestConstants import ExpRewards, NPCIds
from pirates.quest.QuestDNA import QuestDNA
from pirates.quest.QuestLadderDNA import QuestChoiceDNA, \
    QuestChoiceSingleDNA, QuestLadderDNA
from pirates.quest.QuestStatData import QuestStatData

FameQuestLadderDict = {
    'MainStory': QuestLadderDNA(name='MainStory', questInt=1100,
                                firstQuestId='Chapter1.rung1',
                                containers=(QuestLadderDNA(name='Chapter 1'
                                , questInt=1101,
                                firstQuestId='Chapter1.rung1',
                                containers=(QuestDB.QuestDict['Chapter1.rung1'
                                ], QuestDB.QuestDict['Chapter1.rung2'],
                                QuestDB.QuestDict['Chapter1.rung3'])),
                                QuestLadderDNA(name='Chapter 2',
                                questInt=2100,
                                firstQuestId='c2_visit_will_turner',
                                containers=(
        QuestDB.QuestDict['c2_visit_will_turner'],
        QuestDB.QuestDict['c2.2defeatSkeletons'],
        QuestDB.QuestDict['c2_visit_tia_dalma'],
        QuestDB.QuestDict['c2.4recoverOrders'],
        QuestDB.QuestDict['c2.5deliverOrders'],
        QuestDB.QuestDict['c2.9visitDarby'],
        QuestDB.QuestDict['c2.10visitDockworker'],
        QuestDB.QuestDict['c2.11visitBarbossa'],
        )), QuestLadderDNA(name='Chapter 3', questInt=3900,
                           firstQuestId='c3visitJack', containers=(
        QuestDB.QuestDict['c3visitJack'],
        QuestDB.QuestDict['c3visitJoshamee'],
        QuestChoiceDNA(name='c3r1Joshamee', questInt=3901,
                       giverId=NPCIds.JOSHAMEE,
                       containers=(QuestDB.QuestDict['c3r1.1sinkNavyShips'
                       ], QuestDB.QuestDict['c3r1.2defeatNavyGuards'
                       ])),
        QuestLadderDNA(name='c3r2Joshamee', questInt=3902,
                       firstQuestId='c3r2r1Carver',
                       containers=(QuestLadderDNA(name='c3r2r1Carver',
                       questInt=3903,
                       firstQuestId='c3r2r1.1visitScarlet', containers=(
            QuestDB.QuestDict['c3r2r1.1visitScarlet'],
            QuestDB.QuestDict['c3r2r1.3visitCarver'],
            QuestDB.QuestDict['c3r2r1.4deliverGrog'],
            QuestDB.QuestDict['c3r2r1.5visitCarver'],
            QuestDB.QuestDict['c3r2r1.6deliverBonita'],
            QuestDB.QuestDict['c3r2r1.6.5bribeBonita'],
            QuestChoiceDNA(name='c3r2r1r1Tattoo', questInt=3904,
                           giverId=NPCIds.BONITA,
                           containers=(QuestDB.QuestDict['c3r2r1r1.1recoverClaw'
                           ], QuestDB.QuestDict['c3r2r1r1.2recoverRod'
                           ], QuestDB.QuestDict['c3r2r1r1.3recoverBlood'
                           ])),
            QuestDB.QuestDict['c3r2r1.7visitCarver'],
            QuestDB.QuestDict['c3r2r1.8recoverFlag'],
            QuestDB.QuestDict['c3r2r1.9captureSteadman'],
            QuestDB.QuestDict['c3r2r1.10maroonSteadman'],
            QuestDB.QuestDict['c3r2r1.11stealList'],
            QuestDB.QuestDict['c3r2r1.12recoverWarrants'],
            QuestChoiceDNA(name='c3r2r1r2Assassins', questInt=3905,
                           giverId=NPCIds.CARVER,
                           containers=(QuestDB.QuestDict['c3r2r1r2.1Carrou'
                           ], QuestDB.QuestDict['c3r2r1r2.2DArcis'],
                           QuestDB.QuestDict['c3r2r1r2.3Coteau'])),
            QuestDB.QuestDict['c3r2r1.13visitGrog'],
            QuestChoiceDNA(name='c3r2r1r3TattooRemoval', questInt=3906,
                           giverId=NPCIds.DOC_GROG,
                           containers=(QuestDB.QuestDict['c3r2r1r3.1Guano'
                           ], QuestDB.QuestDict['c3r2r1r3.2Hair'],
                           QuestDB.QuestDict['c3r2r1r3.3Blood'])),
            QuestDB.QuestDict['c3r2r1.14deliverRemedy'],
            QuestDB.QuestDict['c3r2r1.14.5stealWarrant'],
            QuestDB.QuestDict['c3r2r1.15visitJoshamee'],
            )), QuestLadderDNA(name='c3r2r2Greer', questInt=3907,
                               firstQuestId='c3r2r2.1visitGreer',
                               containers=(
            QuestDB.QuestDict['c3r2r2.1visitGreer'],
            QuestDB.QuestDict['c3r2r2.2visitBingham'],
            QuestDB.QuestDict['c3r2r2.2.5bribeBingham'],
            QuestDB.QuestDict['c3r2r2.3recoverRum'],
            QuestDB.QuestDict['c3r2r2.4blackjack'],
            QuestDB.QuestDict['c3r2r2.5visitGreer'],
            QuestDB.QuestDict['c3r2r2.6visitBlakeley'],
            QuestDB.QuestDict['c3r2r2.7visitJune'],
            QuestChoiceSingleDNA(name='c3r2r2r8JunesList',
                                 questInt=3908,
                                 firstQuestId='c3r2r2r8r1Ring',
                                 containers=(QuestLadderDNA(name='c3r2r2r8r1Ring'
                                 , questInt=3909,
                                 firstQuestId='c3r2r2r8r1.1visitSmitty'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r2r2r8r1.1visitSmitty'
                                 ],
                                 QuestChoiceDNA(name='c3r2r2r8r1r2RingMaterials'
                                 , questInt=3910,
                                 giverId=NPCIds.JEWELER_SMITTY,
                                 containers=(QuestDB.QuestDict['c3r2r2r8r1r2.1recoverTin'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r1r2.2recoverSand'
                                 ])),
                                 QuestDB.QuestDict['c3r2r2r8r1.3deliverRing'
                                 ])),
                                 QuestLadderDNA(name='c3r2r2r8r2Plates'
                                 , questInt=3911,
                                 firstQuestId='c3r2r2r8r2.1visitCraven'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r2r2r8r2.1visitCraven'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r2.1.5bribeCraven'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r2.2sinkShips'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r2.3sinkNavyShips'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r2.4deliverPlates'
                                 ])),
                                 QuestLadderDNA(name='c3r2r2r8r3Chickens'
                                 , questInt=3912,
                                 firstQuestId='c3r2r2r8r3.1recoverChickens'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r2r2r8r3.1recoverChickens'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r3.2recoverChickens'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r3.3deliverEggs'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r3.4visitJune'
                                 ])))),
            QuestChoiceSingleDNA(name='c3r2r2r8JunesList2',
                                 questInt=3047,
                                 firstQuestId='c3r2r2r8.4recoverPig',
                                 containers=(QuestDB.QuestDict['c3r2r2r8.4recoverPig'
                                 ],
                                 QuestLadderDNA(name='c3r2r2r8r5Necklace'
                                 , questInt=3913,
                                 firstQuestId='c3r2r2r8r5.1visitLucinda'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r2r2r8r5.1visitLucinda'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r5.1.5bribeLucinda'
                                 ],
                                 QuestChoiceDNA(name='c3r2r2r8r5r2NecklaceMaterials'
                                 , questInt=3914,
                                 giverId=NPCIds.LUCINDA,
                                 containers=(QuestDB.QuestDict['c3r2r2r8r5r2.1recoverTeeth'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r5r2.2recoverTeeth'
                                 ])),
                                 QuestDB.QuestDict['c3r2r2r8r5.3deliverNecklace'
                                 ])),
                                 QuestLadderDNA(name='c3r2r2r8r6Doll',
                                 questInt=3915,
                                 firstQuestId='c3r2r2r8r6.1visitGreer',
                                 containers=(
                QuestDB.QuestDict['c3r2r2r8r6.1visitGreer'],
                QuestDB.QuestDict['c3r2r2r8r6.2visitMallet'],
                QuestDB.QuestDict['c3r2r2r8r6.3visitFabiola'],
                QuestDB.QuestDict['c3r2r2r8r6.3.5bribeFabiola'],
                QuestChoiceDNA(name='c3r2r2r8r6r4CurseCure',
                               questInt=3916, giverId=NPCIds.FABIOLA,
                               containers=(QuestDB.QuestDict['c3r2r2r8r6r4.1recoverWings'
                               ],
                               QuestDB.QuestDict['c3r2r2r8r6r4.2recoverScales'
                               ],
                               QuestDB.QuestDict['c3r2r2r8r6r4.3recoverPoison'
                               ])),
                QuestChoiceDNA(name='c3r2r2r8r6r4CurseCure2',
                               questInt=3049, giverId=NPCIds.FABIOLA,
                               containers=(QuestDB.QuestDict['c3r2r2r8r6r4.4recoverClaw'
                               ],
                               QuestDB.QuestDict['c3r2r2r8r6r4.5recoverMud'
                               ])),
                QuestDB.QuestDict['c3r2r2r8r6.5deliverRemedy'],
                QuestDB.QuestDict['c3r2r2r8r6.6visitCarver'],
                QuestDB.QuestDict['c3r2r2r8r6.7deliverGrog'],
                QuestDB.QuestDict['c3r2r2r8r6.8deliverDoll'],
                )))),
            QuestChoiceSingleDNA(name='c3r2r2r8JunesList3',
                                 questInt=3048,
                                 firstQuestId='c3r2r2r8r8Parrot',
                                 containers=(QuestLadderDNA(name='c3r2r2r8r8Parrot'
                                 , questInt=3917,
                                 firstQuestId='c3r2r2r8r8.1visitGreer',
                                 containers=(QuestDB.QuestDict['c3r2r2r8r8.1visitGreer'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r8.2visitOrinda'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r8.3visitTomas'
                                 ],
                                 QuestChoiceSingleDNA(name='c3r2r2r8r8r4Honey'
                                 , questInt=3918,
                                 firstQuestId='c3r2r2r8r8r4.1recoverHoneyShips'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r2r2r8r8r4.1recoverHoneyShips'
                                 ],
                                 QuestLadderDNA(name='c3r2r2r8r8r4r2Bribe'
                                 , questInt=3919,
                                 firstQuestId='c3r2r2r8r8r4r2.1visitMarsh'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r2r2r8r8r4r2.1visitMarsh'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r8r4r2.2bribeMarsh'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r8r4r2.3deliverHoney'
                                 ])))),
                                 QuestDB.QuestDict['c3r2r2r8r8.5deliverParrot'
                                 ])),
                                 QuestLadderDNA(name='c3r2r2r8r9Dice',
                                 questInt=3920,
                                 firstQuestId='c3r2r2r8r9.1visitGreer',
                                 containers=(QuestDB.QuestDict['c3r2r2r8r9.1visitGreer'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r9.2recoverDice'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r9.3deliverDice'
                                 ])),
                                 QuestLadderDNA(name='c3r2r2r8r11Dress'
                                 , questInt=3921,
                                 firstQuestId='c3r2r2r8r11.1visitGreer'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r2r2r8r11.1visitGreer'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r11.2visitCassandra'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r11.3recoverEarrings'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r8r11.4deliverDress'
                                 ])))),
            QuestDB.QuestDict['c3r2r2.9deliverList'],
            QuestChoiceSingleDNA(name='c3r2r2r10GreersWrongs',
                                 questInt=3922,
                                 firstQuestId='c3r2r2r10r1Bowdash',
                                 containers=(QuestLadderDNA(name='c3r2r2r10r1Bowdash'
                                 , questInt=3923,
                                 firstQuestId='c3r2r2r10r1.1visitBowdash'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r2r2r10r1.1visitBowdash'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r10r1.2sinkShips'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r10r1.3visitGreer'
                                 ])),
                                 QuestLadderDNA(name='c3r2r2r10r2Grog',
                                 questInt=3924,
                                 firstQuestId='c3r2r2r10r2.1visitGrog',
                                 containers=(QuestDB.QuestDict['c3r2r2r10r2.1visitGrog'
                                 ],
                                 QuestChoiceDNA(name='c3r2r2r10r2r2Remedy'
                                 , questInt=3925,
                                 giverId=NPCIds.DOC_GROG,
                                 containers=(QuestDB.QuestDict['c3r2r2r10r2r2.1recoverWaspEggs'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r10r2r2.2recoverCrabBile'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r10r2r2.3recoverSaliva'
                                 ])),
                                 QuestDB.QuestDict['c3r2r2r10r2.3recoverRum'
                                 ],
                                 QuestDB.QuestDict['c3r2r2r10r2.4visitGreer'
                                 ])),
                                 QuestLadderDNA(name='c3r2r2r10r3Orinda'
                                 , questInt=3926,
                                 firstQuestId='c3r2r2r10r3.1visitOrinda'
                                 , containers=(
                QuestDB.QuestDict['c3r2r2r10r3.1visitOrinda'],
                QuestDB.QuestDict['c3r2r2r10r3.2captureAlthea'],
                QuestDB.QuestDict['c3r2r2r10r3.3maroonAlthea'],
                QuestDB.QuestDict['c3r2r2r10r3.4visitFlatts'],
                QuestDB.QuestDict['c3r2r2r10r3.5smuggleRum'],
                QuestDB.QuestDict['c3r2r2r10r3.6deliverBracelet'],
                QuestDB.QuestDict['c3r2r2r10r3.7visitGreer'],
                )), QuestLadderDNA(name='c3r2r2r10r4Lucinda',
                                   questInt=3927,
                                   firstQuestId='c3r2r2r10r4.1visitLucinda'
                                   ,
                                   containers=(QuestDB.QuestDict['c3r2r2r10r4.1visitLucinda'
                                   ],
                                   QuestDB.QuestDict['c3r2r2r10r4.2visitDaisy'
                                   ],
                                   QuestDB.QuestDict['c3r2r2r10r4.3recoverNeedles'
                                   ],
                                   QuestDB.QuestDict['c3r2r2r10r4.4visitLucinda'
                                   ],
                                   QuestDB.QuestDict['c3r2r2r10r4.5visitGreer'
                                   ])))),
            QuestDB.QuestDict['c3r2r2.10.5visitJune'],
            QuestDB.QuestDict['c3r2r2.10.51visitBlakeley'],
            QuestDB.QuestDict['c3r2r2.10.52disruptRitual'],
            QuestDB.QuestDict['c3r2r2.10.53visitGreer'],
            QuestDB.QuestDict['c3r2r2.11visitJoshamee'],
            )), QuestLadderDNA(name='c3r2r3Cutts', questInt=3928,
                               firstQuestId='c3r2r3.1visitScarlet',
                               containers=(
            QuestDB.QuestDict['c3r2r3.1visitScarlet'],
            QuestDB.QuestDict['c3r2r3.2recoverEffects'],
            QuestDB.QuestDict['c3r2r3.3visitMillie'],
            QuestDB.QuestDict['c3r2r3.4visitCutts'],
            QuestChoiceSingleDNA(name='c3r2r3r1Pearls', questInt=3929,
                                 firstQuestId='c3r2r3r1.1RecoverSkeletons'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r2r3r1.1RecoverSkeletons'
                                 ],
                                 QuestLadderDNA(name='c3r2r3r1r2Cufflinks'
                                 , questInt=3930,
                                 firstQuestId='c3r2r3r1r2.1visitBowdash'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r2r3r1r2.1visitBowdash'
                                 ],
                                 QuestDB.QuestDict['c3r2r3r1r2.2poker'
                                 ],
                                 QuestDB.QuestDict['c3r2r3r1r2.3poker'
                                 ],
                                 QuestDB.QuestDict['c3r2r3r1r2.4poker'
                                 ],
                                 QuestDB.QuestDict['c3r2r3r1r2.5deliverCutts'
                                 ])),
                                 QuestDB.QuestDict['c3r2r3r1.3recoverShips'
                                 ])),
            QuestChoiceSingleDNA(name='c3r2r3r1Pearls2', questInt=3030,
                                 firstQuestId='c3r2r3r1.4recoverNavy',
                                 containers=(QuestDB.QuestDict['c3r2r3r1.4recoverNavy'
                                 ],
                                 QuestLadderDNA(name='c3r2r3r1r5Smuggler'
                                 , questInt=3931,
                                 firstQuestId='c3r2r3r1r5.1visitOrinda'
                                 , containers=(
                QuestDB.QuestDict['c3r2r3r1r5.1visitOrinda'],
                QuestDB.QuestDict['c3r2r3r1r5.2visitFlatts'],
                QuestDB.QuestDict['c3r2r3r1r5.3sinkNavyShips'],
                QuestDB.QuestDict['c3r2r3r1r5.4recoverArm'],
                QuestDB.QuestDict['c3r2r3r1r5.5visitFabiola'],
                QuestChoiceDNA(name='c3r2r3r1r5r6CurseRemoval',
                               questInt=3932, giverId=NPCIds.FABIOLA,
                               containers=(QuestDB.QuestDict['c3r2r3r1r5r6.1GatorSaliva'
                               ],
                               QuestDB.QuestDict['c3r2r3r1r5r6.2WaspVenom'
                               ],
                               QuestDB.QuestDict['c3r2r3r1r5r6.3ScorpionBlood'
                               ])),
                QuestDB.QuestDict['c3r2r3r1r5.7deliverCutts'],
                )), QuestLadderDNA(name='c3r2r3r1r6Earrings',
                                   questInt=3933,
                                   firstQuestId='c3r2r3r1r6.1visitCarver'
                                   ,
                                   containers=(QuestDB.QuestDict['c3r2r3r1r6.1visitCarver'
                                   ],
                                   QuestDB.QuestDict['c3r2r3r1r6.2visitFabiola'
                                   ],
                                   QuestDB.QuestDict['c3r2r3r1r6.3recoverSkeletonShips'
                                   ],
                                   QuestDB.QuestDict['c3r2r3r1r6.4deliverCutts'
                                   ])))),
            QuestLadderDNA(name='c3r2r3r1r7Alberto', questInt=3934,
                           firstQuestId='c3r2r3r1r7.1visitMallet',
                           containers=(QuestDB.QuestDict['c3r2r3r1r7.1visitMallet'
                           ],
                           QuestDB.QuestDict['c3r2r3r1r7.2deliverFabiola'
                           ],
                           QuestDB.QuestDict['c3r2r3r1r7.3recoverEffects'
                           ],
                           QuestDB.QuestDict['c3r2r3r1r7.4recoverCrabs'
                           ],
                           QuestDB.QuestDict['c3r2r3r1r7.5deliverCutts'
                           ])),
            QuestDB.QuestDict['c3r2r3.8visitJack'],
            QuestDB.QuestDict['c3r2r3.9recoverPapers'],
            QuestDB.QuestDict['c3r2r3.10deliverJack'],
            QuestDB.QuestDict['c3r2r3.11deliverPearl'],
            QuestDB.QuestDict['c3r2r3.12deliverMillie'],
            QuestDB.QuestDict['c3r2r3.13visitCutts'],
            QuestDB.QuestDict['c3r2r3.14visitJoshamee'],
            )), QuestLadderDNA(name='c3r2r4Offrill', questInt=3935,
                               firstQuestId='c3r2r4.1visitCarver',
                               containers=(
            QuestDB.QuestDict['c3r2r4.1visitCarver'],
            QuestDB.QuestDict['c3r2r4.2bribeCarver'],
            QuestDB.QuestDict['c3r2r4.3visitNill'],
            QuestDB.QuestDict['c3r2r4.4blackjack'],
            QuestDB.QuestDict['c3r2r4.5poker'],
            QuestChoiceSingleDNA(name='c3r2r4r6Creditors',
                                 questInt=3936,
                                 firstQuestId='c3r2r4r6r1Grog',
                                 containers=(QuestLadderDNA(name='c3r2r4r6r1Grog'
                                 , questInt=3937,
                                 firstQuestId='c3r2r4r6r1.1visitGrog',
                                 containers=(
                QuestDB.QuestDict['c3r2r4r6r1.1visitGrog'],
                QuestDB.QuestDict['c3r2r4r6r1.2visitCarver'],
                QuestDB.QuestDict['c3r2r4r6r1.3bribeCarver'],
                QuestDB.QuestDict['c3r2r4r6r1.4deliverMedicine'],
                QuestDB.QuestDict['c3r2r4r6r1.5visitMallet'],
                QuestDB.QuestDict['c3r2r4r6r1.6bribeMallet'],
                QuestDB.QuestDict['c3r2r4r6r1.7deliverGrog'],
                QuestDB.QuestDict['c3r2r4r6r1.8deliverJar'],
                QuestDB.QuestDict['c3r2r4r6r1.9deliverJar'],
                QuestDB.QuestDict['c3r2r4r6r1.10visitGrog'],
                QuestDB.QuestDict['c3r2r4r6r1.11recoverCrabs'],
                QuestDB.QuestDict['c3r2r4r6r1.12deliverJar'],
                QuestDB.QuestDict['c3r2r4r6r1.13deliverMoney'],
                QuestDB.QuestDict['c3r2r4r6r1.14deliverPaper'],
                QuestDB.QuestDict['c3r2r4r6r1.15deliverBone'],
                QuestDB.QuestDict['c3r2r4r6r1.16bribeButcher'],
                QuestDB.QuestDict['c3r2r4r6r1.17deliverShavings'],
                QuestDB.QuestDict['c3r2r4r6r1.18recoverBile'],
                QuestDB.QuestDict['c3r2r4r6r1.19deliverBile'],
                QuestDB.QuestDict['c3r2r4r6r1.20deliverPayment'],
                QuestDB.QuestDict['c3r2r4r6r1.21recoverChest'],
                QuestDB.QuestDict['c3r2r4r6r1.22visitNill'],
                )), QuestLadderDNA(name='c3r2r4r6r2Bowdash',
                                   questInt=3938,
                                   firstQuestId='c3r2r4r6r2.1visitBowdash'
                                   , containers=(
                QuestDB.QuestDict['c3r2r4r6r2.1visitBowdash'],
                QuestDB.QuestDict['c3r2r4r6r2.2recoverFlags'],
                QuestDB.QuestDict['c3r2r4r6r2.3captureBillington'],
                QuestDB.QuestDict['c3r2r4r6r2.4maroonBillington'],
                QuestDB.QuestDict['c3r2r4r6r2.5deliverScepter'],
                QuestDB.QuestDict['c3r2r4r6r2.6deliverMap'],
                QuestDB.QuestDict['c3r2r4r6r2.7smuggleRum'],
                QuestDB.QuestDict['c3r2r4r6r2.8visitBowdash'],
                QuestDB.QuestDict['c3r2r4r6r2.9visitJohn'],
                QuestDB.QuestDict['c3r2r4r6r2.10deliverMoney'],
                QuestDB.QuestDict['c3r2r4r6r2.11recoverKey'],
                QuestDB.QuestDict['c3r2r4r6r2.12deliverKey'],
                QuestDB.QuestDict['c3r2r4r6r2.13deliverKey'],
                QuestDB.QuestDict['c3r2r4r6r2.14recoverDiamond'],
                QuestDB.QuestDict['c3r2r4r6r2.15stealCigars'],
                QuestDB.QuestDict['c3r2r4r6r2.16recoverChest'],
                )))),
            QuestDB.QuestDict['c3r2r4.7visitNill'],
            QuestLadderDNA(name='c3r2r4r8Benedek', questInt=3939,
                           firstQuestId='c3r2r4r8.1visitBenedek',
                           containers=(
                QuestDB.QuestDict['c3r2r4r8.1visitBenedek'],
                QuestDB.QuestDict['c3r2r4r8.2captureWallace'],
                QuestDB.QuestDict['c3r2r4r8.3maroonWallace'],
                QuestDB.QuestDict['c3r2r4r8.4deliverMoney'],
                QuestDB.QuestDict['c3r2r4r8.5recoverRum'],
                QuestDB.QuestDict['c3r2r4r8.6visitMarsh'],
                QuestDB.QuestDict['c3r2r4r8.7sinkNavyShips'],
                QuestDB.QuestDict['c3r2r4r8.8visitFlatts'],
                QuestDB.QuestDict['c3r2r4r8.9poker'],
                QuestDB.QuestDict['c3r2r4r8.10deliverMoney'],
                QuestDB.QuestDict['c3r2r4r8.11captureOHenry'],
                QuestDB.QuestDict['c3r2r4r8.12recoverChain'],
                QuestDB.QuestDict['c3r2r4r8.13visitNill'],
                )),
            QuestDB.QuestDict['c3r2r4.9visitJohn'],
            QuestDB.QuestDict['c3r2r4.10deliverDice'],
            QuestDB.QuestDict['c3r2r4.11poker'],
            QuestDB.QuestDict['c3r2r4.12visitJoshamee'],
            )), QuestLadderDNA(name='c3r2r5Grog', questInt=3940,
                               firstQuestId='c3r2r5.1visitGrog',
                               containers=(
            QuestDB.QuestDict['c3r2r5.1visitGrog'],
            QuestChoiceSingleDNA(name='c3r2r5r2Medicine',
                                 questInt=3941,
                                 firstQuestId='c3r2r5r2r1KrakenEye',
                                 containers=(QuestLadderDNA(name='c3r2r5r2r1KrakenEye'
                                 , questInt=3942,
                                 firstQuestId='c3r2r5r2r1.1recoverEyeShips'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r2r5r2r1.1recoverEyeShips'
                                 ],
                                 QuestDB.QuestDict['c3r2r5r2r1.2defeatCrabs'
                                 ],
                                 QuestDB.QuestDict['c3r2r5r2r1.3deliverEye'
                                 ],
                                 QuestDB.QuestDict['c3r2r5r2r1.4bribeBlacksmith'
                                 ],
                                 QuestDB.QuestDict['c3r2r5r2r1.5deliverPowder'
                                 ])),
                                 QuestDB.QuestDict['c3r2r5r2.2recoverCrocwater'
                                 ],
                                 QuestDB.QuestDict['c3r2r5r2.3recoverEntrails'
                                 ])),
            QuestChoiceDNA(name='c3r2r5r2Medicine2', questInt=3031,
                           giverId=NPCIds.DOC_GROG,
                           containers=(QuestDB.QuestDict['c3r2r5r2.4recoverGuano'
                           ],
                           QuestDB.QuestDict['c3r2r5r2.5recoverSplinter'
                           ], QuestDB.QuestDict['c3r2r5r2.6recoverDust'
                           ])),
            QuestChoiceDNA(name='c3r2r5r2Medicine3', questInt=3032,
                           giverId=NPCIds.DOC_GROG,
                           containers=(QuestDB.QuestDict['c3r2r5r2.7recoverEarth'
                           ],
                           QuestDB.QuestDict['c3r2r5r2.8recoverLichens'
                           ], QuestDB.QuestDict['c3r2r5r2.9recoverWater'
                           ])),
            QuestChoiceDNA(name='c3r2r5r2Medicine4', questInt=3034,
                           giverId=NPCIds.DOC_GROG,
                           containers=(QuestDB.QuestDict['c3r2r5r2.10recoverEggs'
                           ],
                           QuestDB.QuestDict['c3r2r5r2.11recoverMoney'
                           ],
                           QuestDB.QuestDict['c3r2r5r2.12recoverNightshade'
                           ],
                           QuestDB.QuestDict['c3r2r5r2.13recoverWhiskers'
                           ])),
            QuestDB.QuestDict['c3r2r5.3deliverJack'],
            QuestDB.QuestDict['c3r2r5.4recoverEyes'],
            QuestDB.QuestDict['c3r2r5.5deliverJack'],
            QuestDB.QuestDict['c3r2r5.6deliverEyes'],
            QuestDB.QuestDict['c3r2r5.7deliverMallet'],
            QuestDB.QuestDict['c3r2r5.8bribeMallet'],
            QuestDB.QuestDict['c3r2r5.9deliverRemedy'],
            QuestDB.QuestDict['c3r2r5.10administerRemedy'],
            QuestDB.QuestDict['c3r2r5.11visitJoshamee'],
            )))),
        QuestDB.QuestDict['c3r2.5.5visitOrinda'],
        QuestDB.QuestDict['c3r2.5captureMontrose'],
        QuestDB.QuestDict['c3r2.6visitCarver'],
        QuestDB.QuestDict['c3r2.7deliverPint'],
        QuestLadderDNA(name='c3r3Joshamee', questInt=3943,
                       firstQuestId='c3r3r1Gunner',
                       containers=(QuestLadderDNA(name='c3r3r1Gunner',
                       questInt=3944, firstQuestId='c3r3r1.1visitOrinda'
                       , containers=(
            QuestDB.QuestDict['c3r3r1.1visitOrinda'],
            QuestDB.QuestDict['c3r3r1.2deliverCargo'],
            QuestDB.QuestDict['c3r3r1.3deliverCoins'],
            QuestDB.QuestDict['c3r3r1.4recoverChest'],
            QuestDB.QuestDict['c3r3r1.5visitDuchamps'],
            QuestDB.QuestDict['c3r3r1.6visitOlivier'],
            QuestDB.QuestDict['c3r3r1.7recoverBarrel'],
            QuestDB.QuestDict['c3r3r1.8deliverBarrel'],
            QuestDB.QuestDict['c3r3r1.9sinkShips'],
            QuestDB.QuestDict['c3r3r1.10sinkShips'],
            QuestDB.QuestDict['c3r3r1.11visitGunner'],
            QuestLadderDNA(name='c3r3r1r12LearnRum', questInt=3945,
                           firstQuestId='c3r3r1r12.1fishRum',
                           containers=(
                QuestDB.QuestDict['c3r3r1r12.1fishRum'],
                QuestDB.QuestDict['c3r3r1r12.2Grog'],
                QuestDB.QuestDict['c3r3r1r12.3lightRum'],
                QuestDB.QuestDict['c3r3r1r12.4darkRum'],
                QuestDB.QuestDict['c3r3r1r12.5fiveYearRum'],
                QuestDB.QuestDict['c3r3r1r12.6tenYearRum'],
                QuestDB.QuestDict['c3r3r1r12.7skeletonRum'],
                )),
            QuestLadderDNA(name='c3r3r1r13Rum', questInt=3946,
                           firstQuestId='c3r3r1r13r1buyRum',
                           containers=(QuestLadderDNA(name='c3r3r1r13r1buyRum'
                           , questInt=3947,
                           firstQuestId='c3r3r1r13r1.1visitRico',
                           containers=(QuestDB.QuestDict['c3r3r1r13r1.1visitRico'
                           ], QuestDB.QuestDict['c3r3r1r13r1.2bribeRico'
                           ],
                           QuestDB.QuestDict['c3r3r1r13r1.3visitGarrett'
                           ],
                           QuestDB.QuestDict['c3r3r1r13r1.4bribeGarrett'
                           ],
                           QuestDB.QuestDict['c3r3r1r13r1.5deliverRum'
                           ])),
                           QuestLadderDNA(name='c3r3r1r13r2stealRum',
                           questInt=3948,
                           firstQuestId='c3r3r1r13r2.1recoverRum',
                           containers=(QuestDB.QuestDict['c3r3r1r13r2.1recoverRum'
                           ],
                           QuestDB.QuestDict['c3r3r1r13r2.2recoverRum'
                           ])), QuestLadderDNA(name='c3r3r1r13r3winRum'
                           , questInt=3949,
                           firstQuestId='c3r3r1r13r3.1poker',
                           containers=(QuestDB.QuestDict['c3r3r1r13r3.1poker'
                           ], QuestDB.QuestDict['c3r3r1r13r3.2blackjack'
                           ])), QuestLadderDNA(name='c3r3r1r13r4makeRum'
                           , questInt=3950,
                           firstQuestId='c3r3r1r13r4.1recoverLadle',
                           containers=(QuestDB.QuestDict['c3r3r1r13r4.1recoverLadle'
                           ],
                           QuestChoiceDNA(name='c3r3r1r13r4r2makeGrog',
                           questInt=3951, giverId=NPCIds.GUNNER,
                           containers=(QuestDB.QuestDict['c3r3r1r13r4r2.1recoverSugar'
                           ],
                           QuestDB.QuestDict['c3r3r1r13r4r2.2recoverWater'
                           ],
                           QuestDB.QuestDict['c3r3r1r13r4r2.3recoverMud'
                           ],
                           QuestDB.QuestDict['c3r3r1r13r4r2.4recoverBottle'
                           ])),
                           QuestChoiceDNA(name='c3r3r1r13r4r3makeLightRum'
                           , questInt=3952, giverId=NPCIds.GUNNER,
                           containers=(QuestDB.QuestDict['c3r3r1r13r4r3.1recoverMolasses'
                           ],
                           QuestDB.QuestDict['c3r3r1r13r4r3.2recoverWater'
                           ],
                           QuestDB.QuestDict['c3r3r1r13r4r3.3recoverVanilla'
                           ],
                           QuestDB.QuestDict['c3r3r1r13r4r3.4recoverBottle'
                           ])),
                           QuestChoiceDNA(name='c3r3r1r13r4r4makeDarkRum'
                           , questInt=3953, giverId=NPCIds.GUNNER,
                           containers=(QuestDB.QuestDict['c3r3r1r13r4r4.1recoverMolasses'
                           ],
                           QuestDB.QuestDict['c3r3r1r13r4r4.2recoverWater'
                           ],
                           QuestDB.QuestDict['c3r3r1r13r4r4.3recoverVanilla'
                           ],
                           QuestDB.QuestDict['c3r3r1r13r4r4.4recoverBottle'
                           ])))))),
            QuestDB.QuestDict['c3r3r1.14deliverRum'],
            QuestDB.QuestDict['c3r3r1.15visitGunner'],
            QuestDB.QuestDict['c3r3r1.16visitPedro'],
            QuestDB.QuestDict['c3r3r1.17bribePedro'],
            QuestDB.QuestDict['c3r3r1.18visitFernando'],
            QuestDB.QuestDict['c3r3r1.19bribeFernando'],
            QuestDB.QuestDict['c3r3r1.20deliverRum'],
            QuestDB.QuestDict['c3r3r1.20.5visitGunner'],
            QuestChoiceSingleDNA(name='c3r3r1r21skeletonRum',
                                 questInt=3954,
                                 firstQuestId='c3r3r1r21r1makeSkeletonRum'
                                 ,
                                 containers=(QuestLadderDNA(name='c3r3r1r21r1makeSkeletonRum'
                                 , questInt=3955,
                                 firstQuestId='c3r3r1r21r1.1visitRomany'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r1r21r1.1visitRomany'
                                 ],
                                 QuestChoiceDNA(name='c3r3r1r21r1r2ingredients'
                                 , questInt=3956,
                                 giverId=NPCIds.ROMANY_BEV, containers=(
                QuestDB.QuestDict['c3r3r1r21r1r2.1recoverMolasses'],
                QuestDB.QuestDict['c3r3r1r21r1r2.2recoverWater'],
                QuestDB.QuestDict['c3r3r1r21r1r2.3recoverDust'],
                QuestDB.QuestDict['c3r3r1r21r1r2.4recoverGas'],
                QuestDB.QuestDict['c3r3r1r21r1r2.5recoverStingers'],
                QuestDB.QuestDict['c3r3r1r21r1r2.6recoverBladder'],
                )))), )),
            QuestDB.QuestDict['c3r3r1.22deliverRum'],
            QuestDB.QuestDict['c3r3r1.23visitGunner'],
            QuestDB.QuestDict['c3r3r1.24visitJoshamee'],
            QuestChoiceSingleDNA(name='c3r3r1r25SingaporeanRum',
                                 questInt=3957,
                                 firstQuestId='c3r3r1r25r1makeSingaporeanRum'
                                 ,
                                 containers=(QuestLadderDNA(name='c3r3r1r25r1makeSingaporeanRum'
                                 , questInt=3958,
                                 firstQuestId='c3r3r1r25r1.1visitCarver'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r1r25r1.1visitCarver'
                                 ],
                                 QuestDB.QuestDict['c3r3r1r25r1.2deliverPint'
                                 ],
                                 QuestChoiceDNA(name='c3r3r1r25r1r3ingredients'
                                 , questInt=3959,
                                 giverId=NPCIds.JOSHAMEE, containers=(
                QuestDB.QuestDict['c3r3r1r25r1r3.1recoverMolasses'],
                QuestDB.QuestDict['c3r3r1r25r1r3.2recoverHoney'],
                QuestDB.QuestDict['c3r3r1r25r1r3.3recoverWater'],
                QuestDB.QuestDict['c3r3r1r25r1r3.4recoverCinnamon'],
                QuestDB.QuestDict['c3r3r1r25r1r3.5recoverCoconut'],
                QuestDB.QuestDict['c3r3r1r25r1r3.6recoverFeather'],
                )))),
                    QuestLadderDNA(name='c3r3r1r25r2stealSingaporeanRum'
                                   , questInt=3960,
                                   firstQuestId='c3r3r1r25r2.1captureArcher'
                                   ,
                                   containers=(QuestDB.QuestDict['c3r3r1r25r2.1captureArcher'
                                   ],
                                   QuestDB.QuestDict['c3r3r1r25r2.2maroonArcher'
                                   ])))),
            QuestDB.QuestDict['c3r3r1.26deliverRum'],
            QuestDB.QuestDict['c3r3r1.27visitGunner'],
            QuestChoiceDNA(name='c3r3r1r28makeVoodooRum',
                           questInt=3961, giverId=NPCIds.GUNNER,
                           containers=(QuestDB.QuestDict['c3r3r1r28.1recoverMolasses'
                           ],
                           QuestDB.QuestDict['c3r3r1r28.2recoverWater'
                           ],
                           QuestDB.QuestDict['c3r3r1r28.3recoverBarnacles'
                           ])),
            QuestChoiceSingleDNA(name='c3r3r1r28makeVoodooRum2',
                                 questInt=3035,
                                 firstQuestId='c3r3r1r28r4hairballs',
                                 containers=(QuestLadderDNA(name='c3r3r1r28r4hairballs'
                                 , questInt=3962,
                                 firstQuestId='c3r3r1r28r4.1visitTomas'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r1r28r4.1visitTomas'
                                 ],
                                 QuestDB.QuestDict['c3r3r1r28r4.2deliverHairballs'
                                 ])),
                                 QuestDB.QuestDict['c3r3r1r28.5recoverFleas'
                                 ],
                                 QuestDB.QuestDict['c3r3r1r28.6recoverTail'
                                 ],
                                 QuestDB.QuestDict['c3r3r1r28.7recoverTooth'
                                 ])),
            QuestDB.QuestDict['c3r3r1.29deliverRum'],
            QuestDB.QuestDict['c3r3r1.30visitGunner'],
            QuestChoiceSingleDNA(name='c3r3r1r31twentyFiveRum',
                                 questInt=3963,
                                 firstQuestId='c3r3r1r31r1Joshamee',
                                 containers=(QuestLadderDNA(name='c3r3r1r31r1Joshamee'
                                 , questInt=3964,
                                 firstQuestId='c3r3r1r31r1.1visitJoshamee'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r1r31r1.1visitJoshamee'
                                 ],
                                 QuestDB.QuestDict['c3r3r1r31r1.2visitBenedek'
                                 ],
                                 QuestDB.QuestDict['c3r3r1r31r1.3recoverEffects'
                                 ])),
                                 QuestLadderDNA(name='c3r3r1r31r2Fernando'
                                 , questInt=3965,
                                 firstQuestId='c3r3r1r31r2.1visitFernando'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r1r31r2.1visitFernando'
                                 ],
                                 QuestChoiceDNA(name='c3r3r1r31r2r2chores'
                                 , questInt=3966,
                                 giverId=NPCIds.FERNANDO,
                                 containers=(QuestDB.QuestDict['c3r3r1r31r2r2.1sinkNavyShips'
                                 ],
                                 QuestDB.QuestDict['c3r3r1r31r2r2.2sinkEITCShips'
                                 ],
                                 QuestDB.QuestDict['c3r3r1r31r2r2.3sinkSkeletonShips'
                                 ])),
                                 QuestChoiceDNA(name='c3r3r1r31r2r2chores2'
                                 , questInt=3036,
                                 giverId=NPCIds.FERNANDO,
                                 containers=(QuestDB.QuestDict['c3r3r1r31r2r2.4smuggleRum'
                                 ],
                                 QuestDB.QuestDict['c3r3r1r31r2r2.5smuggleHoney'
                                 ],
                                 QuestDB.QuestDict['c3r3r1r31r2r2.6smuggleCinnamon'
                                 ])))))),
            QuestDB.QuestDict['c3r3r1.32deliverRum'],
            QuestDB.QuestDict['c3r3r1.33visitGunner'],
            QuestDB.QuestDict['c3r3r1.34visitBarbossa'],
            QuestDB.QuestDict['c3r3r1.35captureTrent'],
            QuestDB.QuestDict['c3r3r1.36maroonTrent'],
            QuestDB.QuestDict['c3r3r1.37deliverKey'],
            QuestDB.QuestDict['c3r3r1.38deliverRum'],
            QuestDB.QuestDict['c3r3r1.39visitGunner'],
            QuestDB.QuestDict['c3r3r1.40captureJones'],
            QuestDB.QuestDict['c3r3r1.41visitMorris'],
            QuestDB.QuestDict['c3r3r1.42visitPedro'],
            QuestDB.QuestDict['c3r3r1.43bribePedro'],
            QuestDB.QuestDict['c3r3r1.44deliverDrink'],
            QuestDB.QuestDict['c3r3r1.45recoverFlags'],
            QuestDB.QuestDict['c3r3r1.46visitPedro'],
            QuestDB.QuestDict['c3r3r1.47bribePedro'],
            QuestDB.QuestDict['c3r3r1.48deliverDrink'],
            QuestDB.QuestDict['c3r3r1.49stealSchedule'],
            QuestDB.QuestDict['c3r3r1.50recoverRum'],
            QuestDB.QuestDict['c3r3r1.51deliverRum'],
            QuestDB.QuestDict['c3r3r1.52visitGunner'],
            QuestDB.QuestDict['c3r3r1.53visitJoshamee'],
            )), QuestLadderDNA(name='c3r3r2Mary', questInt=3967,
                               firstQuestId='c3r3r2.1visitFabiola',
                               containers=(
            QuestDB.QuestDict['c3r3r2.1visitFabiola'],
            QuestDB.QuestDict['c3r3r2.2visitOrinda'],
            QuestDB.QuestDict['c3r3r2.3captureReginald'],
            QuestDB.QuestDict['c3r3r2.4maroonReginald'],
            QuestDB.QuestDict['c3r3r2.5captureDennison'],
            QuestDB.QuestDict['c3r3r2.6maroonDennison'],
            QuestDB.QuestDict['c3r3r2.7captureHedley'],
            QuestDB.QuestDict['c3r3r2.8maroonHedley'],
            QuestDB.QuestDict['c3r3r2.9captureBiggleton'],
            QuestDB.QuestDict['c3r3r2.10maroonBiggleton'],
            QuestDB.QuestDict['c3r3r2.11captureNorman'],
            QuestDB.QuestDict['c3r3r2.12maroonNorman'],
            QuestDB.QuestDict['c3r3r2.13captureFitzpatrick'],
            QuestDB.QuestDict['c3r3r2.14maroonFitzpatrick'],
            QuestDB.QuestDict['c3r3r2.15captureHamilton'],
            QuestDB.QuestDict['c3r3r2.16maroonHamilton'],
            QuestDB.QuestDict['c3r3r2.17visitJohn'],
            QuestDB.QuestDict['c3r3r2.18recoverRum'],
            QuestDB.QuestDict['c3r3r2.19visitMary'],
            QuestChoiceDNA(name='c3r3r2r20revenge', questInt=3968,
                           giverId=NPCIds.SCARY_MARY,
                           containers=(QuestDB.QuestDict['c3r3r2r20.1sinkNavy'
                           ], QuestDB.QuestDict['c3r3r2r20.2sinkEITC'],
                           QuestDB.QuestDict['c3r3r2r20.3sinkSkeleton'
                           ])),
            QuestDB.QuestDict['c3r3r2.20.5recoverBelongings'],
            QuestDB.QuestDict['c3r3r2.21visitJoshamee'],
            )), QuestLadderDNA(name='c3r3r3Giladoga', questInt=3969,
                               firstQuestId='c3r3r3.1visitCarver',
                               containers=(
            QuestDB.QuestDict['c3r3r3.1visitCarver'],
            QuestDB.QuestDict['c3r3r3.2visitMcVane'],
            QuestDB.QuestDict['c3r3r3.3visitGiladoga'],
            QuestDB.QuestDict['c3r3r3.4deliverKey'],
            QuestDB.QuestDict['c3r3r3.5bribeFlinty'],
            QuestDB.QuestDict['c3r3r3.6deliverKey'],
            QuestChoiceSingleDNA(name='c3r3r3r7water', questInt=3970,
                                 firstQuestId='c3r3r3r7r1skeletonWater'
                                 ,
                                 containers=(QuestLadderDNA(name='c3r3r3r7r1skeletonWater'
                                 , questInt=3971,
                                 firstQuestId='c3r3r3r7r1.1visitOrinda'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r3r7r1.1visitOrinda'
                                 ],
                                 QuestDB.QuestDict['c3r3r3r7r1.2recoverWater'
                                 ],
                                 QuestDB.QuestDict['c3r3r3r7r1.3deliverWater'
                                 ])),
                                 QuestLadderDNA(name='c3r3r3r7r2latrineWater'
                                 , questInt=3972,
                                 firstQuestId='c3r3r3r7r2.1visitCarver'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r3r7r2.1visitCarver'
                                 ],
                                 QuestDB.QuestDict['c3r3r3r7r2.2recoverWater'
                                 ],
                                 QuestDB.QuestDict['c3r3r3r7r2.3deliverWater'
                                 ])),
                                 QuestLadderDNA(name='c3r3r3r7r3sharkWater'
                                 , questInt=3973,
                                 firstQuestId='c3r3r3r7r3.1visitBenedek'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r3r7r3.1visitBenedek'
                                 ],
                                 QuestDB.QuestDict['c3r3r3r7r3.2recoverWater'
                                 ],
                                 QuestDB.QuestDict['c3r3r3r7r3.3deliverWater'
                                 ])))),
            QuestChoiceSingleDNA(name='c3r3r3r7water2', questInt=3037,
                                 firstQuestId='c3r3r3r7.4recoverWater',
                                 containers=(QuestDB.QuestDict['c3r3r3r7.4recoverWater'
                                 ],
                                 QuestLadderDNA(name='c3r3r3r7r5cryptWater'
                                 , questInt=3974,
                                 firstQuestId='c3r3r3r7r5.1visitMallet'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r3r7r5.1visitMallet'
                                 ],
                                 QuestDB.QuestDict['c3r3r3r7r5.2bribeMallet'
                                 ],
                                 QuestDB.QuestDict['c3r3r3r7r5.3deliverWater'
                                 ])),
                                 QuestLadderDNA(name='c3r3r3r7r6honeysuckle'
                                 , questInt=3975,
                                 firstQuestId='c3r3r3r7r6.1visitScarlet'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r3r7r6.1visitScarlet'
                                 ],
                                 QuestDB.QuestDict['c3r3r3r7r6.2recoverHoneysuckle'
                                 ],
                                 QuestDB.QuestDict['c3r3r3r7r6.3deliverHoneysuckle'
                                 ])),
                                 QuestLadderDNA(name='c3r3r3r7r7rubber'
                                 , questInt=3976,
                                 firstQuestId='c3r3r3r7r7.1visitBowdash'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r3r7r7.1visitBowdash'
                                 ],
                                 QuestDB.QuestDict['c3r3r3r7r7.2poker'
                                 ],
                                 QuestDB.QuestDict['c3r3r3r7r7.3recoverSap'
                                 ],
                                 QuestDB.QuestDict['c3r3r3r7r7.4deliverSap'
                                 ])))),
            QuestDB.QuestDict['c3r3r3.8deliverKey'],
            QuestLadderDNA(name='c3r3r3r9keys', questInt=3977,
                           firstQuestId='c3r3r3r9r1key', containers=(
                QuestLadderDNA(name='c3r3r3r9r1key', questInt=3978,
                               firstQuestId='c3r3r3r9r1.1visitCraven',
                               containers=(
                    QuestDB.QuestDict['c3r3r3r9r1.1visitCraven'],
                    QuestDB.QuestDict['c3r3r3r9r1.2visitFlatts'],
                    QuestDB.QuestDict['c3r3r3r9r1.3sinkNavyShips'],
                    QuestDB.QuestDict['c3r3r3r9r1.4deliverRum'],
                    QuestDB.QuestDict['c3r3r3r9r1.5deliverMoney'],
                    QuestDB.QuestDict['c3r3r3r9r1.6deliverKey'],
                    )),
                QuestLadderDNA(name='c3r3r3r9r2key', questInt=3979,
                               firstQuestId='c3r3r3r9r2.1visitMallet',
                               containers=(
                    QuestDB.QuestDict['c3r3r3r9r2.1visitMallet'],
                    QuestDB.QuestDict['c3r3r3r9r2.2visitBenedek'],
                    QuestDB.QuestDict['c3r3r3r9r2.3recoverChest'],
                    QuestDB.QuestDict['c3r3r3r9r2.4deliverFabiola'],
                    QuestChoiceDNA(name='c3r3r3r9r2r5ingredients',
                                   questInt=3980,
                                   giverId=NPCIds.FABIOLA,
                                   containers=(QuestDB.QuestDict['c3r3r3r9r2r5.1recoverHair'
                                   ],
                                   QuestDB.QuestDict['c3r3r3r9r2r5.2recoverTears'
                                   ],
                                   QuestDB.QuestDict['c3r3r3r9r2r5.3recoverBlood'
                                   ],
                                   QuestDB.QuestDict['c3r3r3r9r2r5.4recoverGuano'
                                   ])),
                    QuestDB.QuestDict['c3r3r3r9r2.6deliverGold'],
                    QuestDB.QuestDict['c3r3r3r9r2.7recoverCoins'],
                    QuestDB.QuestDict['c3r3r3r9r2.8blackjack'],
                    QuestDB.QuestDict['c3r3r3r9r2.9deliverKey'],
                    )),
                QuestLadderDNA(name='c3r3r3r9r3key', questInt=3981,
                               firstQuestId='c3r3r3r9r3.1visitBowdash',
                               containers=(
                    QuestDB.QuestDict['c3r3r3r9r3.1visitBowdash'],
                    QuestDB.QuestDict['c3r3r3r9r3.2capturePenrod'],
                    QuestDB.QuestDict['c3r3r3r9r3.3maroonPenrod'],
                    QuestDB.QuestDict['c3r3r3r9r3.4deliverGold'],
                    QuestDB.QuestDict['c3r3r3r9r3.5sinkNavyShips'],
                    QuestDB.QuestDict['c3r3r3r9r3.6poker'],
                    QuestDB.QuestDict['c3r3r3r9r3.7deliverKey'],
                    )),
                QuestLadderDNA(name='c3r3r3r9r4key', questInt=3982,
                               firstQuestId='c3r3r3r9r4.1recoverChest',
                               containers=(
                    QuestDB.QuestDict['c3r3r3r9r4.1recoverChest'],
                    QuestDB.QuestDict['c3r3r3r9r4.2visitFabiola'],
                    QuestChoiceDNA(name='c3r3r3r9r4r3oils',
                                   questInt=3983,
                                   giverId=NPCIds.FABIOLA,
                                   containers=(QuestDB.QuestDict['c3r3r3r9r4r3.1recoverCologne'
                                   ],
                                   QuestDB.QuestDict['c3r3r3r9r4r3.2recoverOil'
                                   ],
                                   QuestDB.QuestDict['c3r3r3r9r4r3.3recoverBile'
                                   ])),
                    QuestDB.QuestDict['c3r3r3r9r4.4deliverList'],
                    QuestDB.QuestDict['c3r3r3r9r4.5visitCarver'],
                    QuestDB.QuestDict['c3r3r3r9r4.6bribeCarver'],
                    QuestDB.QuestDict['c3r3r3r9r4.7deliverRum'],
                    QuestDB.QuestDict['c3r3r3r9r4.8visitCarver'],
                    QuestDB.QuestDict['c3r3r3r9r4.9bribeCarver'],
                    QuestDB.QuestDict['c3r3r3r9r4.10deliverRum'],
                    QuestDB.QuestDict['c3r3r3r9r4.11deliverOil'],
                    QuestDB.QuestDict['c3r3r3r9r4.12deliverKey'],
                    )),
                QuestLadderDNA(name='c3r3r3r9r5key', questInt=3984,
                               firstQuestId='c3r3r3r9r5.1visitGrog',
                               containers=(QuestDB.QuestDict['c3r3r3r9r5.1visitGrog'
                               ],
                               QuestChoiceDNA(name='c3r3r3r9r5r2ingredients'
                               , questInt=3985,
                               giverId=NPCIds.DOC_GROG,
                               containers=(QuestDB.QuestDict['c3r3r3r9r5r2.1recoverTeeth'
                               ],
                               QuestDB.QuestDict['c3r3r3r9r5r2.2recoverVenom'
                               ],
                               QuestDB.QuestDict['c3r3r3r9r5r2.3recoverSap'
                               ])),
                               QuestDB.QuestDict['c3r3r3r9r5.3deliverRemedy'
                               ],
                               QuestDB.QuestDict['c3r3r3r9r5.4recoverKey'
                               ],
                               QuestDB.QuestDict['c3r3r3r9r5.5deliverKey'
                               ])),
                QuestLadderDNA(name='c3r3r3r9r6key', questInt=3986,
                               firstQuestId='c3r3r3r9r6.1visitAnne',
                               containers=(QuestDB.QuestDict['c3r3r3r9r6.1visitAnne'
                               ],
                               QuestDB.QuestDict['c3r3r3r9r6.2defeatSkeletons'
                               ],
                               QuestDB.QuestDict['c3r3r3r9r6.3deliverKey'
                               ])),
                QuestLadderDNA(name='c3r3r3r9r7key', questInt=3987,
                               firstQuestId='c3r3r3r9r7.1visitScarlet',
                               containers=(
                    QuestDB.QuestDict['c3r3r3r9r7.1visitScarlet'],
                    QuestDB.QuestDict['c3r3r3r9r7.2captureCollier'],
                    QuestDB.QuestDict['c3r3r3r9r7.3maroonCollier'],
                    QuestDB.QuestDict['c3r3r3r9r7.4deliverNecklace'],
                    QuestDB.QuestDict['c3r3r3r9r7.5bribeScarlet'],
                    QuestDB.QuestDict['c3r3r3r9r7.6deliverKey'],
                    )),
                QuestLadderDNA(name='c3r3r3r9r8key', questInt=3988,
                               firstQuestId='c3r3r3r9r8.1recoverOrders'
                               , containers=(
                    QuestDB.QuestDict['c3r3r3r9r8.1recoverOrders'],
                    QuestDB.QuestDict['c3r3r3r9r8.2visitBlakeley'],
                    QuestDB.QuestDict['c3r3r3r9r8.3visitWoodruff'],
                    QuestDB.QuestDict['c3r3r3r9r8.4recoverSalve'],
                    QuestDB.QuestDict['c3r3r3r9r8.5deliverWax'],
                    QuestDB.QuestDict['c3r3r3r9r8.6bribeFabiola'],
                    QuestDB.QuestDict['c3r3r3r9r8.7deliverKey'],
                    QuestDB.QuestDict['c3r3r3r9r8.8recoverKey'],
                    QuestDB.QuestDict['c3r3r3r9r8.9deliverKey'],
                    )),
                )),
            QuestDB.QuestDict['c3r3r3.10recoverChest'],
            QuestDB.QuestDict['c3r3r3.11visitJack'],
            QuestDB.QuestDict['c3r3r3.12recoverKey'],
            QuestDB.QuestDict['c3r3r3.13deliverKey'],
            QuestDB.QuestDict['c3r3r3.14visitJoshamee'],
            )), QuestLadderDNA(name='c3r3r4Smith', questInt=3989,
                               firstQuestId='c3r3r4.1visitBowdash',
                               containers=(
            QuestDB.QuestDict['c3r3r4.1visitBowdash'],
            QuestDB.QuestDict['c3r3r4.2visitSmith'],
            QuestChoiceSingleDNA(name='c3r3r4r3starboardHull',
                                 questInt=3990,
                                 firstQuestId='c3r3r4r3r1build',
                                 containers=(QuestLadderDNA(name='c3r3r4r3r1build'
                                 , questInt=3991,
                                 firstQuestId='c3r3r4r3r1.1recoverMeat'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r4r3r1.1recoverMeat'
                                 ],
                                 QuestChoiceDNA(name='c3r3r4r3r1r2materials'
                                 , questInt=3992,
                                 giverId=NPCIds.JOHN_SMITH,
                                 containers=(QuestDB.QuestDict['c3r3r4r3r1r2.1recoverWood'
                                 ],
                                 QuestDB.QuestDict['c3r3r4r3r1r2.2recoverNails'
                                 ],
                                 QuestDB.QuestDict['c3r3r4r3r1r2.3recoverNails'
                                 ],
                                 QuestDB.QuestDict['c3r3r4r3r1r2.4recoverPitch'
                                 ])))), )),
            QuestDB.QuestDict['c3r3r4.3.5visitSmith'],
            QuestChoiceSingleDNA(name='c3r3r4r4portHull',
                                 questInt=3995,
                                 firstQuestId='c3r3r4r4r1build',
                                 containers=(QuestLadderDNA(name='c3r3r4r4r1build'
                                 , questInt=3996,
                                 firstQuestId='c3r3r4r4r1.1recoverMeat'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r4r4r1.1recoverMeat'
                                 ],
                                 QuestChoiceDNA(name='c3r3r4r4r1r2materials'
                                 , questInt=3997,
                                 giverId=NPCIds.JOHN_SMITH,
                                 containers=(QuestDB.QuestDict['c3r3r4r4r1r2.1recoverWood'
                                 ],
                                 QuestDB.QuestDict['c3r3r4r4r1r2.2recoverNails'
                                 ],
                                 QuestDB.QuestDict['c3r3r4r4r1r2.3recoverBeams'
                                 ],
                                 QuestDB.QuestDict['c3r3r4r4r1r2.4recoverBolts'
                                 ])))), )),
            QuestDB.QuestDict['c3r3r4.4.5visitSmith'],
            QuestChoiceSingleDNA(name='c3r3r4r5cabin', questInt=3999,
                                 firstQuestId='c3r3r4r5r1build',
                                 containers=(QuestLadderDNA(name='c3r3r4r5r1build'
                                 , questInt=3040,
                                 firstQuestId='c3r3r4r5r1.1recoverMeat'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r4r5r1.1recoverMeat'
                                 ],
                                 QuestChoiceDNA(name='c3r3r4r5r1r2materials'
                                 , questInt=3041,
                                 giverId=NPCIds.JOHN_SMITH,
                                 containers=(QuestDB.QuestDict['c3r3r4r5r1r2.1recoverWood'
                                 ],
                                 QuestDB.QuestDict['c3r3r4r5r1r2.2recoverNails'
                                 ])))), )),
            QuestDB.QuestDict['c3r3r4.5.5visitSmith'],
            QuestChoiceSingleDNA(name='c3r3r4r6masts', questInt=3043,
                                 firstQuestId='c3r3r4r6r1build',
                                 containers=(QuestLadderDNA(name='c3r3r4r6r1build'
                                 , questInt=3044,
                                 firstQuestId='c3r3r4r6r1.1recoverMeat'
                                 ,
                                 containers=(QuestDB.QuestDict['c3r3r4r6r1.1recoverMeat'
                                 ],
                                 QuestChoiceDNA(name='c3r3r4r6r1r2materials'
                                 , questInt=3045,
                                 giverId=NPCIds.JOHN_SMITH,
                                 containers=(QuestDB.QuestDict['c3r3r4r6r1r2.1recoverBeams'
                                 ],
                                 QuestDB.QuestDict['c3r3r4r6r1r2.2recoverBolts'
                                 ])))), )),
            QuestDB.QuestDict['c3r3r4.7visitSmith'],
            QuestDB.QuestDict['c3r3r4.8recoverSails'],
            QuestDB.QuestDict['c3r3r4.9recoverRopes'],
            QuestDB.QuestDict['c3r3r4.10recoverCannons'],
            QuestDB.QuestDict['c3r3r4.11recoverFigure'],
            QuestDB.QuestDict['c3r3r4.12recoverRum'],
            QuestDB.QuestDict['c3r3r4.12.5visitBowdash'],
            QuestDB.QuestDict['c3r3r4.12.51recoverKey'],
            QuestDB.QuestDict['c3r3r4.12.52visitSmith'],
            QuestDB.QuestDict['c3r3r4.13visitJoshamee'],
            )))),
        QuestDB.QuestDict['c3.4captureMontrose'],
        QuestDB.QuestDict['c3.5maroonMontrose'],
        QuestDB.QuestDict['c3.6deliverMap'],
        QuestDB.QuestDict['c3.7recoverPearl'],
        QuestDB.QuestDict['c3.8visitJack'],
        )))),
    'WeaponDoll': QuestLadderDNA(name='WeaponDoll', questInt=19900,
                                 firstQuestId='wd.1visitTia',
                                 containers=(QuestDB.QuestDict['wd.1visitTia'
                                 ], QuestChoiceDNA(name='wdr2Materials'
                                 , questInt=19901,
                                 giverId=NPCIds.TIA_DALMA,
                                 containers=(QuestDB.QuestDict['wdr2.1recoverStraw'
                                 ],
                                 QuestDB.QuestDict['wdr2.2recoverPitch'
                                 ],
                                 QuestDB.QuestDict['wdr2.3recoverSilk'
                                 ],
                                 QuestDB.QuestDict['wdr2.4recoverWire'
                                 ])), QuestChoiceDNA(name='wdr4blood',
                                 questInt=19902,
                                 giverId=NPCIds.TIA_DALMA,
                                 containers=(QuestDB.QuestDict['wdr4.1bloodOfRockCrab'
                                 ],
                                 QuestDB.QuestDict['wdr4.2bloodOfScorpion'
                                 ],
                                 QuestDB.QuestDict['wdr4.3bloodOfAlligator'
                                 ], QuestDB.QuestDict['wdr4.4bloodOfBat'
                                 ],
                                 QuestDB.QuestDict['wdr4.5bloodOfWasp'
                                 ])), QuestChoiceDNA(name='wdr6BoneDust'
                                 , questInt=19903,
                                 giverId=NPCIds.TIA_DALMA,
                                 containers=(QuestDB.QuestDict['wdr6.1boneDustOfClod'
                                 ],
                                 QuestDB.QuestDict['wdr6.2boneDustOfSludge'
                                 ],
                                 QuestDB.QuestDict['wdr6.3boneDustOfMire'
                                 ],
                                 QuestDB.QuestDict['wdr6.4boneDustOfMuck'
                                 ])))),
    'WeaponDagger': QuestLadderDNA(name='WeaponDagger', questInt=19905,
                                   firstQuestId='wk.1visitElizabeth',
                                   containers=(
        QuestDB.QuestDict['wk.1visitElizabeth'],
        QuestDB.QuestDict['wk.2visitWill'],
        QuestChoiceDNA(name='wkr3Materials', questInt=19906,
                       giverId=NPCIds.WILL_TURNER,
                       containers=(QuestDB.QuestDict['wkr3.1recoverSteel'
                       ], QuestDB.QuestDict['wkr3.2recoverSilver'],
                       QuestDB.QuestDict['wkr3.3recoverBone'],
                       QuestDB.QuestDict['wkr3.4recoverTongs'],
                       QuestDB.QuestDict['wkr3.5recoverCoal'])),
        QuestDB.QuestDict['wk.4visitElizabeth'],
        QuestDB.QuestDict['wk.5recoverMessage'],
        QuestDB.QuestDict['wk.6visitWill'],
        QuestDB.QuestDict['wk.7deliverKnives'],
        )),
    'WeaponGrenade': QuestLadderDNA(name='WeaponGrenade',
                                    questInt=19700,
                                    firstQuestId='wg.1visitJack',
                                    containers=(
        QuestDB.QuestDict['wg.1visitJack'],
        QuestDB.QuestDict['wg.2visitEwan'],
        QuestChoiceDNA(name='wgr3Materials', questInt=19701,
                       giverId=NPCIds.EWAN,
                       containers=(QuestDB.QuestDict['wgr3.1recoverSaltpeter'
                       ], QuestDB.QuestDict['wgr3.2recoverCharcoal'],
                       QuestDB.QuestDict['wgr3.3recoverSulfur'])),
        QuestChoiceDNA(name='wgr4Materials', questInt=19702,
                       giverId=NPCIds.EWAN,
                       containers=(QuestDB.QuestDict['wgr4.1recoverFuses'
                       ], QuestDB.QuestDict['wgr4.2recoverFlints'],
                       QuestDB.QuestDict['wgr4.3recoverCasings'])),
        QuestDB.QuestDict['wg.5recoverTar'],
        QuestDB.QuestDict['wg.6sinkShips'],
        QuestChoiceDNA(name='wgr7Smuggle', questInt=19903,
                       giverId=NPCIds.EWAN,
                       containers=(QuestDB.QuestDict['wgr7.1smuggleBombs'
                       ], QuestDB.QuestDict['wgr7.2deliverBombs'])),
        QuestDB.QuestDict['wg.8deliverBombs'],
        )),
    'WeaponStaff': QuestLadderDNA(name='WeaponStaff', questInt=19950,
                                  firstQuestId='ws.1visitTia',
                                  containers=(
        QuestDB.QuestDict['ws.1visitTia'],
        QuestChoiceDNA(name='wsr2Heart', questInt=19951,
                       giverId=NPCIds.TIA_DALMA,
                       containers=(QuestDB.QuestDict['wsr2.1defeatCorpse'
                       ], QuestDB.QuestDict['wsr2.2defeatCarrion'],
                       QuestDB.QuestDict['wsr2.3defeatZombie'])),
        QuestDB.QuestDict['ws.3recoverStump'],
        QuestDB.QuestDict['ws.4recoverHead'],
        QuestChoiceDNA(name='wsr3PowerUp', questInt=19952,
                       giverId=NPCIds.TIA_DALMA, containers=(
            QuestDB.QuestDict['wsr3.1defeatWasp'],
            QuestDB.QuestDict['wsr3.2defeatGator'],
            QuestDB.QuestDict['wsr3.3defeatScorpion'],
            QuestDB.QuestDict['wsr3.4defeatCrab'],
            QuestDB.QuestDict['wsr3.5defeatFlyTrap'],
            QuestDB.QuestDict['wsr3.6defeatBat'],
            )),
        QuestChoiceDNA(name='wsr4EveryShore', questInt=19953,
                       giverId=NPCIds.TIA_DALMA, containers=(
            QuestDB.QuestDict['wsr4.1defeatPortRoyal'],
            QuestDB.QuestDict['wsr4.2defeatTortuga'],
            QuestDB.QuestDict['wsr4.3defeatPadresDelFuego'],
            QuestDB.QuestDict['wsr4.4defeatKingshead'],
            QuestDB.QuestDict['wsr4.5defeatCuba'],
            QuestDB.QuestDict['wsr4.6defeatRumrunners'],
            QuestDB.QuestDict['wsr4.4defeatDriftwood'],
            QuestDB.QuestDict['wsr4.5defeatCangrejos'],
            QuestDB.QuestDict['wsr4.6defeatPerdida'],
            QuestDB.QuestDict['wsr4.4defeatCutthroat'],
            QuestDB.QuestDict['wsr4.5defeatTormenta'],
            QuestDB.QuestDict['wsr4.6defeatOutkast'],
            QuestDB.QuestDict['wsr4.6defeatAnvil'],
            )),
        QuestDB.QuestDict['ws.5deliverDoll'],
        )),
    'VoodooDollUnlockL5': QuestLadderDNA(
        name='VoodooDollUnlockL5',
        questInt=2351,
        giverId=NPCIds.TIA_DALMA,
        firstQuestId='vdul5.1visitTia',
        droppable=False,
        containers=(
            QuestDB.QuestDict['vdul5.1visitTia'],
            QuestChoiceDNA(name='vdul5r1Heirlooms', questInt=2352,
                           giverId=NPCIds.TIA_DALMA,
                           containers=(QuestDB.QuestDict['vdul5r1.1acquireArmor'
                           ], QuestDB.QuestDict['vdul5r1.2acquireHair'
                           ], QuestDB.QuestDict['vdul5r1.3findEarring'
                           ])),
            QuestChoiceDNA(name='vdul5r2FirstGeneral', questInt=2353,
                           giverId=NPCIds.TIA_DALMA,
                           containers=(QuestDB.QuestDict['vdul5r2.1defeatUndead'
                           ],
                           QuestDB.QuestDict['vdul5r2.2defeatGeneralBloodless'
                           ])),
            QuestChoiceDNA(name='vdul5r3SecondGeneral', questInt=2354,
                           giverId=NPCIds.TIA_DALMA,
                           containers=(QuestDB.QuestDict['vdul5r3.1defeatUndead'
                           ],
                           QuestDB.QuestDict['vdul5r3.2defeatGeneralHex'
                           ])),
            QuestChoiceDNA(name='vdul5r4ThirdGeneral', questInt=2355,
                           giverId=NPCIds.TIA_DALMA,
                           containers=(QuestDB.QuestDict['vdul5r4.1defeatUndead'
                           ],
                           QuestDB.QuestDict['vdul5r4.2defeatGeneralSandspine'
                           ])),
            QuestChoiceDNA(name='vdul5r2FinalGeneral', questInt=2356,
                           giverId=NPCIds.TIA_DALMA,
                           containers=(QuestDB.QuestDict['vdul5r5.1defeatUndead'
                           ],
                           QuestDB.QuestDict['vdul5r5.2defeatGeneralDarkhart'
                           ])),
            ),
        ),
    'VoodooStaffUnlockL5': QuestLadderDNA(
        name='VoodooStaffUnlockL5',
        questInt=2500,
        giverId=NPCIds.ROLAND_RAGGART,
        firstQuestId='vsul5.1visitRoland',
        droppable=False,
        containers=(
            QuestDB.QuestDict['vsul5.1visitRoland'],
            QuestDB.QuestDict['vsul5.2captureEITCCaptain'],
            QuestDB.QuestDict['vsul5.3visitRoland'],
            QuestDB.QuestDict['vsul5.4maroonEITCCaptain'],
            QuestDB.QuestDict['vsul5.5retrieveStatuettes'],
            QuestDB.QuestDict['vsul5.6acquireHighLevelUndeadBones'],
            QuestChoiceDNA(name='vsul5r1EITCItems', questInt=2501,
                           giverId=NPCIds.ROLAND_RAGGART,
                           containers=(QuestDB.QuestDict['vsul5r1.1acquireEITCBadge'
                           ],
                           QuestDB.QuestDict['vsul5r1.2acquireGoldHandleRapier'
                           ])),
            QuestChoiceDNA(name='vsul5r2VariousEITC', questInt=2502,
                           giverId=NPCIds.ROLAND_RAGGART,
                           containers=(QuestDB.QuestDict['vsul5r2.1defeatThugs'
                           ], QuestDB.QuestDict['vsul5r2.2defeatGrunts'
                           ],
                           QuestDB.QuestDict['vsul5r2.3defeatHiredGuns'
                           ],
                           QuestDB.QuestDict['vsul5r2.4defeatMercenaries'
                           ],
                           QuestDB.QuestDict['vsul5r2.5defeatAssassins'
                           ])),
            ),
        ),
    'DaggerUnlockL5': QuestLadderDNA(
        name='DaggerUnlockL5',
        questInt=2450,
        giverId=NPCIds.FERRERA,
        firstQuestId='dul5.1visitFerrar',
        droppable=False,
        containers=(
            QuestDB.QuestDict['dul5.1visitFerrar'],
            QuestDB.QuestDict['dul5.2findNecklace'],
            QuestDB.QuestDict['dul5.3visitOrinda'],
            QuestDB.QuestDict['dul5.4defeatExHusband'],
            QuestDB.QuestDict['dul5.5visitMcKidd'],
            QuestDB.QuestDict['dul5.6captureSwain'],
            QuestDB.QuestDict['dul5.7maroonSwain'],
            QuestDB.QuestDict['dul5.8visitTia'],
            QuestDB.QuestDict['dul5.9defeatWitchdoctorBoss'],
            QuestDB.QuestDict['dul5.10visitGrimm'],
            QuestDB.QuestDict['dul5.10.5bribeGrimm'],
            QuestDB.QuestDict['dul5.11findDaggers'],
            QuestDB.QuestDict['dul5.12visitFerrar'],
            ),
        ),
    'PistolUnlockL5': QuestLadderDNA(
        name='PistolUnlockL5',
        questInt=2300,
        giverId=NPCIds.ERASMUS_GRIMSDITCH,
        firstQuestId='pul5.1visitErasmus',
        droppable=False,
        containers=(
            QuestDB.QuestDict['pul5.1visitErasmus'],
            QuestDB.QuestDict['pul5.2acquirePistolParts'],
            QuestDB.QuestDict['pul5.3visitDelilah'],
            QuestDB.QuestDict['pul5.4defeatFormerLove'],
            QuestDB.QuestDict['pul5.5findGems'],
            QuestDB.QuestDict['pul5.6acquireWoodStocks'],
            QuestDB.QuestDict['pul5.7deliverToErasmus'],
            QuestChoiceDNA(name='pul5r1Tasks', questInt=2301,
                           giverId=NPCIds.ERASMUS_GRIMSDITCH,
                           containers=(QuestDB.QuestDict['pul5r1.1acquireCopper'
                           ],
                           QuestDB.QuestDict['pul5r1.2acquireGunPowder'
                           ],
                           QuestDB.QuestDict['pul5r1.3defeatAlligatorBoss'
                           ])),
            ),
        ),
    'CutlassUnlockL5': QuestLadderDNA(
        name='CutlassUnlockL5',
        questInt=2400,
        giverId=NPCIds.BALTHASAR,
        firstQuestId='cul5.1visitBalthasar',
        droppable=False,
        containers=(
            QuestDB.QuestDict['cul5.1visitBalthasar'],
            QuestChoiceDNA(name='cul5r1ShipParts', questInt=2401,
                           giverId=NPCIds.BALTHASAR,
                           containers=(QuestDB.QuestDict['cul5r1.1acquireSailcloth'
                           ],
                           QuestDB.QuestDict['cul5r1.2acquireWoodPlanks'
                           ], QuestDB.QuestDict['cul5r1.3acquireRopes'
                           ], QuestDB.QuestDict['cul5r1.4acquireRigging'
                           ])),
            QuestDB.QuestDict['cul5.2visitMiguel'],
            QuestDB.QuestDict['cul5.3defeatUndeadFrench'],
            QuestDB.QuestDict['cul5.4visitPhillip'],
            QuestChoiceDNA(name='cul5r2SwordParts', questInt=2402,
                           giverId=NPCIds.PHILLIP_FULLER,
                           containers=(QuestDB.QuestDict['cul5r2.1findNavySteel'
                           ],
                           QuestDB.QuestDict['cul5r2.2acquireBoneHandle'
                           ])),
            QuestDB.QuestDict['cul5.5defeatBossScorpion'],
            QuestDB.QuestDict['cul5.6visitGrog'],
            QuestDB.QuestDict['cul5.7visitFuller'],
            ),
        ),
    }
FortuneQuestLadderDict = {
    'TreasureRogues': QuestLadderDNA(name='TreasureRogues',
            questInt=19907, firstQuestId='tr.1visitElizabeth',
            containers=(QuestDB.QuestDict['tr.1visitElizabeth'],
            QuestDB.QuestDict['tr.2captureLuther'],
            QuestDB.QuestDict['tr.3visitElizabeth'])),
    'TreasureRogues2': QuestLadderDNA(name='TreasureRogues2',
            questInt=19908, firstQuestId='tr2.1deliverPaintings',
            containers=(QuestDB.QuestDict['tr2.1deliverPaintings'], )),
    'TreasureTeeth': QuestLadderDNA(name='TreasureTeeth',
                                    questInt=19909,
                                    firstQuestId='tt.1visitJack',
                                    containers=(QuestDB.QuestDict['tt.1visitJack'
                                    ],
                                    QuestDB.QuestDict['tt.2recoverTooth'
                                    ])),
    'TreasureTeeth2': QuestLadderDNA(name='TreasureTeeth2',
            questInt=19910, firstQuestId='tt2.1deliverTeeth',
            containers=(QuestDB.QuestDict['tt2.1deliverTeeth'],
            QuestDB.QuestDict['tt2.2recoverGold'])),
    'TreasureMedals': QuestLadderDNA(name='TreasureMedals',
            questInt=19911, firstQuestId='tm.1visitWill',
            containers=(QuestDB.QuestDict['tm.1visitWill'], )),
    'TreasureMedals2': QuestLadderDNA(name='TreasureMedals2',
            questInt=19912, firstQuestId='tm2.1deliverMedals',
            containers=(QuestDB.QuestDict['tm2.1deliverMedals'],
            QuestDB.QuestDict['tm2.2recoverReagent'])),
    'TreasureRings': QuestLadderDNA(name='TreasureRings',
                                    questInt=19913,
                                    firstQuestId='trr.1visitBarbossa',
                                    containers=(QuestDB.QuestDict['trr.1visitBarbossa'
                                    ], )),
    'TreasureRings2': QuestLadderDNA(name='TreasureRings2',
            questInt=19914, firstQuestId='trr2.1deliverRings',
            containers=(QuestDB.QuestDict['trr2.1deliverRings'],
            QuestDB.QuestDict['trr2.2recoverRing'])),
    'TreasureChess': QuestLadderDNA(name='TreasureChess',
                                    questInt=19915,
                                    firstQuestId='tc.1visitJoshamee',
                                    containers=(QuestDB.QuestDict['tc.1visitJoshamee'
                                    ], QuestDB.QuestDict['tc.2poker'
                                    ])),
    'TreasureChess2': QuestLadderDNA(name='TreasureChess2',
            questInt=19916, firstQuestId='tc2.1deliverChess',
            containers=(QuestDB.QuestDict['tc2.1deliverChess'], )),
    'TreasureFigurines': QuestLadderDNA(name='TreasureFigurines',
            questInt=19917, firstQuestId='tf.1visitTia',
            containers=(QuestDB.QuestDict['tf.1visitTia'], )),
    'TreasureFigurines2': QuestLadderDNA(name='TreasureFigurines2',
            questInt=19918, firstQuestId='tf2.1deliverFigurines',
            containers=(QuestDB.QuestDict['tf2.1deliverFigurines'], )),
    'BlackMack': QuestLadderDNA(
        name='BlackMack',
        questInt=19919,
        giverId=NPCIds.BLACK_MACK,
        firstQuestId='ccbm.1poker',
        droppable=True,
        containers=(QuestDB.QuestDict['ccbm.1poker'],
                    QuestDB.QuestDict['ccbm.2defeatSkeleton']),
        ),
    'TeleportTotem': QuestLadderDNA(name='TeleportTotem',
                                    questInt=19920,
                                    firstQuestId='tptr1.1visitTia',
                                    containers=(QuestDB.QuestDict['tpt.1visitTia'
                                    ],
                                    QuestChoiceDNA(name='tptr2Payment',
                                    questInt=19921,
                                    giverId=NPCIds.TIA_DALMA,
                                    containers=(QuestDB.QuestDict['tptr1.1recoverBat'
                                    ],
                                    QuestDB.QuestDict['tptr1.2recoverWasp'
                                    ],
                                    QuestDB.QuestDict['tptr1.3recoverLeaf'
                                    ])),
                                    QuestDB.QuestDict['tpt.2recoverArtifact'
                                    ])),
    'TPT_PortRoyalUnlock': QuestLadderDNA(name='TPT_PortRoyalUnlock',
            questInt=19730, firstQuestId='tptpr.1visitLucinda',
            containers=(QuestDB.QuestDict['tptpr.1visitLucinda'],
            QuestDB.QuestDict['tptpr.2gainLucindaTrust'],
            QuestDB.QuestDict['tptpr.3gainLucindaTrustAgain'],
            QuestDB.QuestDict['tptpr.4recoverFirstMedal'])),
    'TPT_CubaUnlock': QuestLadderDNA(name='TPT_CubaUnlock',
            questInt=19740, firstQuestId='tptc.1visitTiaDalma',
            containers=(QuestDB.QuestDict['tptc.1visitTiaDalma'],
            QuestChoiceDNA(name='tptcPayment', questInt=19741,
            giverId=NPCIds.TIA_DALMA,
            containers=(QuestDB.QuestDict['tptcr1.1NavyCoats'],
            QuestDB.QuestDict['tptcr1.2FlyTrapRoots'])))),
    'TPT_PadresDelFuegoUnlock': QuestLadderDNA(name='TPT_PadresDelFuegoUnlock'
            , questInt=19750, firstQuestId='tptpdf.1visitRomany',
            containers=(QuestDB.QuestDict['tptpdf.1visitRomany'],
            QuestChoiceDNA(name='tptpdfPayment', questInt=19751,
            giverId=NPCIds.ROMANY_BEV,
            containers=(QuestDB.QuestDict['tptpdfr1.1FaceWeakUndead'],
            QuestDB.QuestDict['tptpdfr1.2FaceStrongerUndead'],
            QuestDB.QuestDict['tptpdfr1.3FaceStrongUndead'])),
            QuestDB.QuestDict['tptpdf.2FindArtifact'])),
    'PortRoyalPCTier1': QuestLadderDNA(name='PortRoyalPCTier1',
            questInt=19940, giverId=NPCIds.SHANE_MCGREENY,
            firstQuestId='cards.prt1.defeatCadets',
            containers=(QuestDB.QuestDict['cards.prt1.defeatCadets'],
            QuestDB.QuestDict['cards.prt1.retrievekey'])),
    'PortRoyalPCTier2': QuestLadderDNA(name='PortRoyalPCTier2',
            questInt=19760, giverId=NPCIds.SHANE_MCGREENY,
            firstQuestId='cards.prt2.recoverNavyMuskets',
            containers=(QuestDB.QuestDict['cards.prt2.recoverNavyMuskets'
            ], QuestChoiceDNA(name='PortRoyalPCTier2Tasks',
            questInt=19761, giverId=NPCIds.SHANE_MCGREENY,
            containers=(QuestDB.QuestDict['cards.prt2.recoverNavyCoats'
            ], QuestDB.QuestDict['cards.prt2.recoverNavyPants'],
            QuestDB.QuestDict['cards.prt2.recoverABadge'])),
            QuestDB.QuestDict['cards.prt2.recoverLocationDocument'])),
    'PortRoyalPCTier3': QuestLadderDNA(name='PortRoyalPCTier3',
            questInt=19944, giverId=NPCIds.SHANE_MCGREENY,
            firstQuestId='cards.prt3.stealGuardSchedule', containers=(
        QuestDB.QuestDict['cards.prt3.stealGuardSchedule'],
        QuestDB.QuestDict['cards.prt3.defeatVeterans'],
        QuestDB.QuestDict['cards.prt3.stealShipSchedule'],
        QuestDB.QuestDict['cards.prt3.captureCaptain'],
        QuestDB.QuestDict['cards.prt3.maroonCaptain'],
        QuestDB.QuestDict['cards.prt3.startCrimeWave'],
        QuestDB.QuestDict['cards.prt3.getReward'],
        )),
    'WatkinsErrand1': QuestLadderDNA(name='WatkinsErrand1',
            questInt=19922, giverId=NPCIds.BARTHOLOMEW_WATKINS,
            droppable=True,
            containers=(QuestDB.QuestDict['bw1.1recoverpowder'], )),
    'WatkinsErrand2': QuestLadderDNA(name='WatkinsErrand2',
            questInt=19923, giverId=NPCIds.BARTHOLOMEW_WATKINS,
            droppable=True,
            containers=(QuestDB.QuestDict['bw1.1recovercotton'], )),
    'WatkinsErrand3': QuestLadderDNA(name='WatkinsErrand3',
            questInt=19924, giverId=NPCIds.BARTHOLOMEW_WATKINS,
            droppable=True,
            containers=(QuestDB.QuestDict['bw1.1recoveriron'], )),
    'LucindaErrands': QuestLadderDNA(
        name='LucindaErrands',
        questInt=19925,
        giverId=NPCIds.LUCINDA,
        firstQuestId='lu1.recovercrabshells',
        droppable=True,
        containers=(QuestDB.QuestDict['lu1.recovercrabshells'],
                    QuestDB.QuestDict['lu1.recoveralligatortails'],
                    QuestDB.QuestDict['lu1.recoverscorpionblood']),
        ),
    'DarbyDrydocksTasks': QuestLadderDNA(
        name='DarbyDrydocksTasks',
        questInt=19926,
        giverId=NPCIds.DARBY_DRYDOCK,
        firstQuestId='dd1.recoverwood',
        droppable=True,
        containers=(QuestDB.QuestDict['dd1.recoverwood'],
                    QuestDB.QuestDict['dd1.recoveriron'],
                    QuestDB.QuestDict['dd1.recovercopper'],
                    QuestDB.QuestDict['dd1.recovercloth']),
        ),
    'JosieMcReedyErrands': QuestLadderDNA(
        name='JosieMcReedyErrands',
        questInt=19928,
        giverId=NPCIds.JOSIE_MCKEEDY,
        firstQuestId='jm1.1recoverrumbarrels',
        droppable=True,
        containers=(QuestDB.QuestDict['jm1.1recoverrumbarrels'],
                    QuestDB.QuestDict['jm1.3recoverwhiskeybarrels'],
                    QuestDB.QuestDict['jm1.5recoverglasses'],
                    QuestDB.QuestDict['jm1.7recoverhoney']),
        ),
    'RSmithErrands': QuestLadderDNA(
        name='RSmithErrands',
        questInt=19930,
        giverId=NPCIds.R_SMITH_PEWTERER,
        firstQuestId='rs1.1recovertools',
        droppable=True,
        containers=(QuestDB.QuestDict['rs1.1recovertools'],
                    QuestDB.QuestDict['rs1.3recoveriron'],
                    QuestDB.QuestDict['rs1.5recovercoal']),
        ),
    'PeterChipparrAssailant': QuestLadderDNA(
        name='PeterChipparrAssailant',
        questInt=19932,
        giverId=NPCIds.PETER_CHIPPARR,
        firstQuestId='pc.1visitSam',
        droppable=True,
        containers=(
            QuestDB.QuestDict['pc.1visitSam'],
            QuestDB.QuestDict['pc.2visitPeter'],
            QuestDB.QuestDict['pc.3QuestionNavyOfficers'],
            QuestDB.QuestDict['pc.5FindNavySwine'],
            QuestDB.QuestDict['pc.6MaroonNavySwine'],
            QuestDB.QuestDict['pc.7visitPeter3'],
            ),
        ),
    'MercJob1': QuestLadderDNA(name='MercJob1', questInt=19933,
                               giverId=NPCIds.JOSIE_MCREEDY,
                               droppable=True,
                               containers=(QuestDB.QuestDict['mercenary_job'
                               ], )),
    'MercJob2': QuestLadderDNA(name='MercJob2', questInt=19934,
                               giverId=NPCIds.JOSIE_MCREEDY,
                               droppable=True,
                               containers=(QuestDB.QuestDict['naval_mercenary_job'
                               ], )),
    'MercJob3': QuestLadderDNA(name='MercJob3', questInt=19935,
                               giverId=NPCIds.JOHNNY_MCVANE,
                               droppable=True,
                               containers=(QuestDB.QuestDict['mercenary_job_tortuga'
                               ], )),
    'MercJob4': QuestLadderDNA(name='MercJob4', questInt=19937,
                               giverId=NPCIds.JOHNNY_MCVANE,
                               droppable=True,
                               containers=(QuestDB.QuestDict['naval_mercenary_job_tortuga'
                               ], )),
    'MercJobEM': QuestLadderDNA(name='MercJobEM', questInt=20032,
                                giverId=NPCIds.CAPTAIN_JOB,
                                droppable=True,
                                containers=(QuestDB.QuestDict['mercenary_job_em'
                                ], )),
    'SeabonesErrand2': QuestLadderDNA(name='SeabonesErrand2',
            questInt=19941, giverId=NPCIds.SAM_SEABONES,
            droppable=True, containers=(QuestDB.QuestDict['0'], )),
    'SeabonesErrand3': QuestLadderDNA(name='SeabonesErrand3',
            questInt=19942, giverId=NPCIds.SAM_SEABONES,
            droppable=True,
            containers=(QuestDB.QuestDict['1141416661.17sdnaik'],
            QuestDB.QuestDict['1141781456.75sdnaik'])),
    'SeabonesErrand4': QuestLadderDNA(name='SeabonesErrand4',
            questInt=19943, giverId=NPCIds.SAM_SEABONES,
            droppable=True, containers=(QuestDB.QuestDict['2'], )),
    'PerlaAlodiaJewels': QuestLadderDNA(
        name='PerlaAlodiaJewels',
        questInt=24000,
        giverId=NPCIds.PERLA_ALODIA,
        firstQuestId='pa1.trackDownJewels',
        droppable=True,
        containers=(
            QuestDB.QuestDict['pa1.trackDownJewels'],
            QuestDB.QuestDict['pa1.bribeOlivier'],
            QuestDB.QuestDict['pa1.gatherRubyStones'],
            QuestDB.QuestDict['pa1.gatherAmethystStones'],
            QuestDB.QuestDict['pa1.gatherSapphireStones'],
            QuestDB.QuestDict['pa1.defeatPerlasEnemy'],
            ),
        ),
    'PerlaAlodiaTrouble': QuestLadderDNA(
        name='PerlaAlodiaTrouble',
        questInt=24600,
        giverId=NPCIds.PERLA_ALODIA,
        firstQuestId='pa2.visitOlivier',
        droppable=True,
        containers=(QuestDB.QuestDict['pa2.visitOlivier'],
                    QuestChoiceDNA(name='pa2.recoverFlags',
                    questInt=24604, giverId=NPCIds.OLIVIER,
                    containers=(QuestDB.QuestDict['pa2.recoverNavyFlags'
                    ], QuestDB.QuestDict['pa2.recoverEITCFlags'])),
                    QuestChoiceDNA(name='pa2.recoverClothes',
                    questInt=24609, giverId=NPCIds.OLIVIER,
                    containers=(QuestDB.QuestDict['pa2.recoverNavyCoats'
                    ], QuestDB.QuestDict['pa2.recoverNavyPants'],
                    QuestDB.QuestDict['pa2.recoverEITCCoats'],
                    QuestDB.QuestDict['pa2.recoverEITCPants'])),
                    QuestChoiceDNA(name='pa2.recoverSupplies',
                    questInt=24614, giverId=NPCIds.OLIVIER,
                    containers=(QuestDB.QuestDict['pa2.recoverWarrants'
                    ], QuestDB.QuestDict['pa2.recoverPrisonKeys'],
                    QuestDB.QuestDict['pa2.recoverSchedule'])),
                    QuestDB.QuestDict['pa2.visitPerla']),
        ),
    'DajinMingJewels': QuestLadderDNA(
        name='DajinMingJewels',
        questInt=24100,
        giverId=NPCIds.DAJIN_MING,
        firstQuestId='dm1.visitJohnnyMcvane',
        droppable=True,
        containers=(
            QuestDB.QuestDict['dm1.visitJohnnyMcvane'],
            QuestDB.QuestDict['dm1.visitOrindaLeJeune'],
            QuestDB.QuestDict['dm1.sinkFirstEITCShip'],
            QuestChoiceDNA(name='dm1.defeatEITCShips', questInt=24101,
                           giverId=NPCIds.ORINDA,
                           containers=(QuestDB.QuestDict['dm1.sinkEITCShipA'
                           ], QuestDB.QuestDict['dm1.sinkEITCShipB'],
                           QuestDB.QuestDict['dm1.sinkEITCShipC'],
                           QuestDB.QuestDict['dm1.sinkEITCShipD'])),
            QuestDB.QuestDict['dm1.visitDajinMing'],
            QuestDB.QuestDict['dm1.defeatNavyShips'],
            QuestDB.QuestDict['dm1.visitOrindaLeJeune2'],
            ),
        ),
    'DajinMingsCompetition': QuestLadderDNA(
        name='DajinMingsCompetition',
        questInt=24700,
        giverId=NPCIds.DAJIN_MING,
        firstQuestId='dm2.recoverShopApplication',
        droppable=True,
        containers=(
            QuestDB.QuestDict['dm2.recoverShopApplication'],
            QuestDB.QuestDict['dm2.deliverShopApplication'],
            QuestDB.QuestDict['dm2.visitBoatswainBill'],
            QuestDB.QuestDict['dm2.recoverCoinBag'],
            QuestDB.QuestDict['dm2.deliverCoinBag'],
            QuestChoiceDNA(name='dm2.recoverFarmAnimals',
                           questInt=24708, giverId=NPCIds.BIG_PHIL,
                           containers=(QuestDB.QuestDict['dm2.recoverChickens'
                           ], QuestDB.QuestDict['dm2.recoverPigs'])),
            QuestDB.QuestDict['dm2.visitBoatswainBill2'],
            QuestDB.QuestDict['dm2.visitSeamstressAnne'],
            QuestChoiceDNA(name='dm2.recoverHides', questInt=24714,
                           giverId=NPCIds.SEAMSTRESS_ANNE,
                           containers=(QuestDB.QuestDict['dm2.recoverAlligatorHides'
                           ],
                           QuestDB.QuestDict['dm2.recoverFlyTrapHides'
                           ], QuestDB.QuestDict['dm2.recoverBatHides'
                           ])),
            QuestDB.QuestDict['dm2.visitBoatswainBill3'],
            QuestDB.QuestDict['dm2.deliverContract'],
            QuestDB.QuestDict['dm2.defeatEITC'],
            ),
        ),
    'JewelerSmittyDebt': QuestLadderDNA(
        name='JewelerSmittyDebt',
        questInt=24200,
        giverId=NPCIds.JEWELER_SMITTY,
        firstQuestId='js1.visitBingham',
        droppable=True,
        containers=(
            QuestDB.QuestDict['js1.visitBingham'],
            QuestChoiceDNA(name='js1.defeatBinghamsList',
                           questInt=24207, giverId=NPCIds.BINGHAM,
                           containers=(QuestDB.QuestDict['js1.defeatBinghamListA'
                           ], QuestDB.QuestDict['js1.defeatBinghamListB'
                           ], QuestDB.QuestDict['js1.defeatBinghamListC'
                           ], QuestDB.QuestDict['js1.defeatBinghamListD'
                           ], QuestDB.QuestDict['js1.defeatBinghamListE'
                           ])),
            QuestDB.QuestDict['js1.visitJimWavemonger'],
            QuestChoiceDNA(name='js1.defeatWavemongersList',
                           questInt=24213,
                           giverId=NPCIds.JIM_WAVEMONGER,
                           containers=(QuestDB.QuestDict['js1.defeatWarmongerListA'
                           ],
                           QuestDB.QuestDict['js1.defeatWarmongerListB'
                           ],
                           QuestDB.QuestDict['js1.defeatWarmongerListC'
                           ],
                           QuestDB.QuestDict['js1.defeatWarmongerListD'
                           ])),
            QuestDB.QuestDict['js1.visitBingham2'],
            QuestDB.QuestDict['js1.visitJewelerSmitty'],
            ),
        ),
    'SmittyIsSick': QuestLadderDNA(
        name='SmittyIsSick',
        questInt=24800,
        giverId=NPCIds.SARAH,
        firstQuestId='js2.visitSmitty',
        droppable=True,
        containers=(
            QuestDB.QuestDict['js2.visitSmitty'],
            QuestDB.QuestDict['js2.deliverBloodSample'],
            QuestDB.QuestDict['js2.deliverList'],
            QuestDB.QuestDict['js2.bribeEdward'],
            QuestChoiceDNA(name='js2.gatherMedicalSupplies',
                           questInt=24808, giverId=NPCIds.SARAH,
                           containers=(QuestDB.QuestDict['js2.recoverMedicine'
                           ], QuestDB.QuestDict['js2.recoverBandages'],
                           QuestDB.QuestDict['js2.recoverMedicalTools'
                           ])),
            QuestDB.QuestDict['js2.findSmittysStuff'],
            QuestDB.QuestDict['js2.deliverMessage'],
            QuestDB.QuestDict['js2.defeatNavyGuards'],
            ),
        ),
    'SpecialInk': QuestLadderDNA(
        name='SpecialInk',
        questInt=24300,
        giverId=NPCIds.SOLOMON_ODOUGAL,
        firstQuestId='sd1.visitLucinda',
        droppable=True,
        containers=(
            QuestDB.QuestDict['sd1.visitLucinda'],
            QuestChoiceDNA(name='sd1.collectingIngredients',
                           questInt=24315, giverId=NPCIds.LUCINDA,
                           containers=(QuestDB.QuestDict['sd1.recoverGatorSaliva'
                           ], QuestDB.QuestDict['sd1.recoverNeedle'],
                           QuestDB.QuestDict['sd1.recoverBoneDust'],
                           QuestDB.QuestDict['sd1.recoverSulfur'],
                           QuestDB.QuestDict['sd1.recoverBlood'])),
            QuestDB.QuestDict['sd1.visitJimWavemonger'],
            QuestDB.QuestDict['sd1.recoverCursedWood'],
            QuestDB.QuestDict['sd1.deliverFineInk'],
            QuestDB.QuestDict['sd1.visitWilliamTurk'],
            QuestChoiceDNA(name='sd1.playingCards', questInt=24313,
                           giverId=NPCIds.WILLIAM_TURK,
                           containers=(QuestDB.QuestDict['sd1.playPoker'
                           ], QuestDB.QuestDict['sd1.playBlackjack'])),
            QuestDB.QuestDict['sd1.deliverTattooPattern'],
            ),
        ),
    'ShipLegend': QuestLadderDNA(
        name='ShipLegend',
        questInt=25100,
        giverId=NPCIds.SOLOMON_ODOUGAL,
        firstQuestId='sd2.deliverTattooPattern',
        droppable=True,
        containers=(
            QuestDB.QuestDict['sd2.deliverTattooPattern'],
            QuestDB.QuestDict['sd2.findShipLog'],
            QuestDB.QuestDict['sd2.visitSolomon'],
            QuestDB.QuestDict['sd2.recoverFamilyHeirlooms'],
            QuestDB.QuestDict['sd2.visitBingham'],
            QuestDB.QuestDict['sd2.bribeBingham'],
            QuestDB.QuestDict['sd2.deliverList'],
            QuestDB.QuestDict['sd2.defeatEITC'],
            QuestChoiceDNA(name='familyPaintings', questInt=25111,
                           giverId=NPCIds.SOLOMON_ODOUGAL,
                           containers=(QuestDB.QuestDict['sd2.findPaintingsA'
                           ], QuestDB.QuestDict['sd2.findPaintingsB'],
                           QuestDB.QuestDict['sd2.findPaintingsC'])),
            QuestDB.QuestDict['sd2.deliverPainting'],
            ),
        ),
    'LovelsNeighbor': QuestLadderDNA(
        name='LovelsNeighbor',
        questInt=24400,
        giverId=NPCIds.LALA_LOVEL,
        firstQuestId='ll1.visitButcherBrown',
        droppable=True,
        containers=(
            QuestDB.QuestDict['ll1.visitButcherBrown'],
            QuestChoiceDNA(name='ll1.gatherMeat', questInt=24402,
                           giverId=NPCIds.BUTCHER_BROWN,
                           containers=(QuestDB.QuestDict['ll1.recoverAlligatorMeat'
                           ], QuestDB.QuestDict['ll1.recoverFlyTrapMeat'
                           ],
                           QuestDB.QuestDict['ll1.recoverSkeletonMeat'
                           ],
                           QuestDB.QuestDict['ll1.recoverRockCrabMeat'
                           ], QuestDB.QuestDict['ll1.recoverBatMeat'
                           ])),
            QuestDB.QuestDict['ll1.visitLala'],
            QuestDB.QuestDict['ll1.visitFabiola'],
            QuestChoiceDNA(name='ll1.gatherGypsySupplies',
                           questInt=24414, giverId=NPCIds.FABIOLA,
                           containers=(QuestDB.QuestDict['ll1.recoverBoneDust'
                           ], QuestDB.QuestDict['ll1.recoverWax'],
                           QuestDB.QuestDict['ll1.recoverTar'],
                           QuestDB.QuestDict['ll1.recoverBattleSaltWater'
                           ])),
            QuestDB.QuestDict['ll1.visitLala2'],
            QuestDB.QuestDict['ll1.visitBlacksmithFlinty'],
            QuestDB.QuestDict['ll1.recoverIronBars'],
            QuestDB.QuestDict['ll1.visitLala3'],
            ),
        ),
    'LalaLovelsBrother': QuestLadderDNA(
        name='LalaLovelsBrother',
        questInt=25000,
        giverId=NPCIds.LALA_LOVEL,
        firstQuestId='ll2.visitSlim',
        droppable=True,
        containers=(
            QuestDB.QuestDict['ll2.visitSlim'],
            QuestDB.QuestDict['ll2.deliverCoinBag'],
            QuestDB.QuestDict['ll2.recoverDiary'],
            QuestChoiceDNA(name='ll2.cleanupWildwoods', questInt=25008,
                           giverId=NPCIds.JACK_REDRAT,
                           containers=(QuestDB.QuestDict['ll2.defeatWildWoodA'
                           ], QuestDB.QuestDict['ll2.defeatWildWoodB'],
                           QuestDB.QuestDict['ll2.defeatWildWoodC'],
                           QuestDB.QuestDict['ll2.defeatWildWoodD'])),
            QuestChoiceDNA(name='ll2.buildWildwoods', questInt=25014,
                           giverId=NPCIds.JACK_REDRAT,
                           containers=(QuestDB.QuestDict['ll2.recoverPlanks'
                           ], QuestDB.QuestDict['ll2.recoverNails'],
                           QuestDB.QuestDict['ll2.recoverSaw'],
                           QuestDB.QuestDict['ll2.recoverBeams'],
                           QuestDB.QuestDict['ll2.recoverTin'])),
            QuestDB.QuestDict['ll2.visitLala'],
            ),
        ),
    'HelpingMercedesCorazon': QuestLadderDNA(
        name='HelpingMercedesCorazon',
        questInt=24500,
        giverId=NPCIds.MERCEDES_CORAZON,
        firstQuestId='mc1.visitShochettPrymme',
        droppable=True,
        containers=(
            QuestDB.QuestDict['mc1.visitShochettPrymme'],
            QuestChoiceDNA(name='mc1.ShochettsList', questInt=24515,
                           giverId=NPCIds.SHOCHETT_PRYMME, containers=(
                QuestDB.QuestDict['mc1.defeatSkeletons'],
                QuestDB.QuestDict['mc1.defeatVampireBat'],
                QuestDB.QuestDict['mc1.defeatFlyTrapsA'],
                QuestDB.QuestDict['mc1.defeatFlyTrapsB'],
                QuestDB.QuestDict['mc1.defeatDreadScorpions'],
                QuestDB.QuestDict['mc1.defeatAlligators'],
                )),
            QuestDB.QuestDict['mc1.recoverEITCList'],
            QuestDB.QuestDict['mc1.deliverDocument'],
            QuestDB.QuestDict['mc1.bribeRico'],
            QuestDB.QuestDict['mc1.recoverInformation'],
            QuestDB.QuestDict['mc1.recoverDeskKey'],
            QuestDB.QuestDict['mc1.recoverDeed'],
            QuestDB.QuestDict['mc1.deliverDeed'],
            ),
        ),
    'BlackMarketInks': QuestLadderDNA(
        name='BlackMarketInks',
        questInt=24900,
        giverId=NPCIds.MERCEDES_CORAZON,
        firstQuestId='mc2.visitFernando',
        droppable=True,
        containers=(
            QuestDB.QuestDict['mc2.visitFernando'],
            QuestDB.QuestDict['mc2.playBlackjack'],
            QuestChoiceDNA(name='mc2.exoticInk', questInt=24905,
                           giverId=NPCIds.MERCEDES_CORAZON,
                           containers=(QuestDB.QuestDict['mc2.recoverVenom'
                           ], QuestDB.QuestDict['mc2.recoverClaw'],
                           QuestDB.QuestDict['mc2.recoverBoneDust'])),
            QuestChoiceDNA(name='mc2.tattooInfection', questInt=24909,
                           giverId=NPCIds.MERCEDES_CORAZON,
                           containers=(QuestDB.QuestDict['mc2.recoverBarnacles'
                           ], QuestDB.QuestDict['mc2.recoverSaltWater'
                           ], QuestDB.QuestDict['mc2.recoverCursedWood'
                           ])),
            QuestDB.QuestDict['mc2.deliverSalve'],
            QuestDB.QuestDict['mc2.visitMercedes'],
            ),
        ),
    'PirateLore': QuestLadderDNA(
        name='PirateLore',
        questInt=25400,
        giverId=NPCIds.WILL_TURNER,
        firstQuestId='wt1.visitWillTurner',
        droppable=False,
        containers=(
            QuestDB.QuestDict['wt1.visitWillTurner'],
            QuestDB.QuestDict['wt1.deliverPirateLorePage'],
            QuestDB.QuestDict['wt1.recoverChestOfPirateLore'],
            QuestDB.QuestDict['wt1.deliverMedal'],
            QuestDB.QuestDict['wt1.recoverEITCManual'],
            QuestChoiceDNA(name='recoverLorePages', questInt=25409,
                           giverId=NPCIds.WILL_TURNER,
                           containers=(QuestDB.QuestDict['wt1.recoverLorePagesA'
                           ], QuestDB.QuestDict['wt1.recoverLorePagesB'
                           ], QuestDB.QuestDict['wt1.recoverLorePagesC'
                           ], QuestDB.QuestDict['wt1.recoverLorePagesD'
                           ])),
            QuestDB.QuestDict['wt1.deliverUnfinishedBookOfPirateLore'],
            QuestChoiceDNA(name='GettingMckiddsAttention',
                           questInt=25413, giverId=NPCIds.BILLY_MCKIDD,
                           containers=(QuestDB.QuestDict['wt1.playPoker'
                           ], QuestDB.QuestDict['wt1.playBlackjack'])),
            QuestChoiceDNA(name='QuidProQuo', questInt=25419,
                           giverId=NPCIds.BILLY_MCKIDD,
                           containers=(QuestDB.QuestDict['wt1.defeatSkeletons'
                           ], QuestDB.QuestDict['wt1.defeatFlyTraps'],
                           QuestDB.QuestDict['wt1.defeatBigGators'],
                           QuestDB.QuestDict['wt1.defeatGiantCrabs'],
                           QuestDB.QuestDict['wt1.defeatWasps'])),
            QuestChoiceDNA(name='PuttingItAllTogether', questInt=25423,
                           giverId=NPCIds.WILL_TURNER,
                           containers=(QuestDB.QuestDict['wt1.recoverRestOfBookA'
                           ], QuestDB.QuestDict['wt1.recoverRestOfBookB'
                           ], QuestDB.QuestDict['wt1.recoverRestOfBookC'
                           ])),
            QuestDB.QuestDict['wt1.deliverBookOfLore'],
            ),
        ),
    'FeatsOfStrength': QuestLadderDNA(
        name='FeatsOfStrength',
        questInt=25300,
        giverId=NPCIds.JOHN_WALLACE,
        firstQuestId='jw1.visitJohnWallace',
        droppable=False,
        containers=(
            QuestDB.QuestDict['jw1.visitJohnWallace'],
            QuestDB.QuestDict['jw1.visitBingham'],
            QuestDB.QuestDict['jw1.deliverShipPlans'],
            QuestDB.QuestDict['jw1.visitBingham2'],
            QuestDB.QuestDict['jw1.deliverBackgroundCheck'],
            QuestChoiceDNA(name='IntroFeats', questInt=25306,
                           giverId=NPCIds.JOHN_WALLACE,
                           containers=(QuestDB.QuestDict['jw1.defeatWasps'
                           ], QuestDB.QuestDict['jw1.defeatScorpions'],
                           QuestDB.QuestDict['jw1.defeatSkeletons'],
                           QuestDB.QuestDict['jw1.defeatCrabs'],
                           QuestDB.QuestDict['jw1.defeatAlligators'])),
            QuestDB.QuestDict['jw1.visitShochett'],
            QuestChoiceDNA(name='ShochettsHides', questInt=25315,
                           giverId=NPCIds.SHOCHETT_PRYMME,
                           containers=(QuestDB.QuestDict['jw1.recoverHidesA'
                           ], QuestDB.QuestDict['jw1.recoverHidesB'],
                           QuestDB.QuestDict['jw1.recoverHidesC'],
                           QuestDB.QuestDict['jw1.recoverBoneDust'])),
            QuestDB.QuestDict['jw1.deliverFineSteelBars'],
            QuestChoiceDNA(name='BladeIngredients', questInt=25320,
                           giverId=NPCIds.JOHN_WALLACE,
                           containers=(QuestDB.QuestDict['jw1.recoverCursedWood'
                           ],
                           QuestDB.QuestDict['jw1.recoverLeatherStraps'
                           ],
                           QuestDB.QuestDict['jw1.recoverBladeSharpener'
                           ])),
            QuestDB.QuestDict['jw1.recoverArrestWarrant'],
            ),
        ),
    'GoodForBusiness': QuestLadderDNA(
        name='GoodForBusiness',
        questInt=25200,
        giverId=NPCIds.ALEXANDER_THAYER,
        firstQuestId='at1.0visitThayer',
        droppable=False,
        containers=(
            QuestDB.QuestDict['at1.0visitThayer'],
            QuestDB.QuestDict['at1.visitBingham'],
            QuestDB.QuestDict['at1.returnOrder'],
            QuestDB.QuestDict['at1.deliverOrderA'],
            QuestDB.QuestDict['at1.deliverOrderB'],
            QuestDB.QuestDict['at1.deliverOrderC'],
            QuestDB.QuestDict['at1.deliverOrderD'],
            QuestDB.QuestDict['at1.deliverOrderE'],
            QuestDB.QuestDict['at1.deliverOrderF'],
            QuestDB.QuestDict['at1.visitThayer'],
            QuestChoiceDNA(name='AttractingCustomers', questInt=25211,
                           giverId=NPCIds.ALEXANDER_THAYER,
                           containers=(QuestDB.QuestDict['at1.playPoker'
                           ], QuestDB.QuestDict['at1.playBlackjack'])),
            QuestChoiceDNA(name='StoreEndorsement', questInt=25217,
                           giverId=NPCIds.ALEXANDER_THAYER,
                           containers=(QuestDB.QuestDict['at1.defeatBigAlligators'
                           ], QuestDB.QuestDict['at1.defeatSkeletons'],
                           QuestDB.QuestDict['at1.defeatFlyTrap'],
                           QuestDB.QuestDict['at1.defeatVampireBat'],
                           QuestDB.QuestDict['at1.defeatScorpion'])),
            QuestChoiceDNA(name='StirringUpTrouble', questInt=25220,
                           giverId=NPCIds.ALEXANDER_THAYER,
                           containers=(QuestDB.QuestDict['at1.defeatNavy'
                           ], QuestDB.QuestDict['at1.defeatEITC'])),
            QuestDB.QuestDict['at1.recoverAntiquePistols'],
            ),
        ),
    'VoodooDollUnlockL4': QuestLadderDNA(
        name='VoodooDollUnlockL4',
        questInt=4100,
        giverId=NPCIds.TIA_DALMA,
        firstQuestId='vdu4.0visitTiaDalma',
        droppable=False,
        containers=(
            QuestDB.QuestDict['vdu4.0visitTiaDalma'],
            QuestDB.QuestDict['vdu4.1visitRomanyBev'],
            QuestDB.QuestDict['vdu4.2returnToTia'],
            QuestChoiceDNA(name='ConstructLocationSpell',
                           questInt=4101, giverId=NPCIds.TIA_DALMA,
                           containers=(
                QuestDB.QuestDict['vdu4r1.1acquireMastsOfSunkenShips'],
                QuestDB.QuestDict['vdu4r1.2acquireSkeletonBones'],
                QuestDB.QuestDict['vdu4r1.3acquirePortRoyalBattleEarth'
                                  ],
                QuestDB.QuestDict['vdu4r1.4acquireTortugaBattleEarth'],
                QuestDB.QuestDict['vdu4r1.5acquirePadresDelFuegoBattleEarth'
                                  ],
                QuestDB.QuestDict['vdu4r1.6acquireKingsheadBattleEarth'
                                  ],
                QuestDB.QuestDict['vdu4r1.7acquireCubaBattleEarth'],
                QuestDB.QuestDict['vdu4r1.8acquireRumrunnersBattleEarth'
                                  ],
                QuestDB.QuestDict['vdu4r1.9acquireDriftwoodBattleEarth'
                                  ],
                QuestDB.QuestDict['vdu4r1.10acquireCangrejosBattleEarth'
                                  ],
                QuestDB.QuestDict['vdu4r1.11acquirePerdidaBattleEarth'
                                  ],
                QuestDB.QuestDict['vdu4r1.12acquireCutthroatBattleEarth'
                                  ],
                QuestDB.QuestDict['vdu4r1.13acquireTormentaBattleEarth'
                                  ],
                QuestDB.QuestDict['vdu4r1.14acquireOutkastBattleEarth'
                                  ],
                QuestDB.QuestDict['vdu4r1.15acquireAnvilBattleEarth'],
                )),
            QuestDB.QuestDict['vdu4.4retrieveFirstPieceOfRelic'],
            QuestDB.QuestDict['vdu4.5retrieveRestOfPiecesOfRelic'],
            QuestChoiceDNA(name='ConstructDestructionSpell',
                           questInt=4102, giverId=NPCIds.TIA_DALMA,
                           containers=(
                QuestDB.QuestDict['vdu4r2.1retrieveScorpionVenom'],
                QuestDB.QuestDict['vdu4r2.2retrieveAlligatorTeeth'],
                QuestDB.QuestDict['vdu4r2.3retrieveWaspStinger'],
                QuestDB.QuestDict['vdu4r2.4retrieveCrabClaw'],
                QuestDB.QuestDict['vdu4r2.5retrieveBatClaw'],
                QuestDB.QuestDict['vdu4r2.6retrieveBattleSaltWater'],
                )),
            QuestDB.QuestDict['vdu4.6returnToTia'],
            ),
        ),
    'VoodooStaffUnlockL4': QuestLadderDNA(
        name='VoodooStaffUnlockL4',
        questInt=4145,
        giverId=NPCIds.TIA_DALMA,
        firstQuestId='vsu4.0visitTiaDalma',
        droppable=False,
        containers=(
            QuestDB.QuestDict['vsu4.0visitTiaDalma'],
            QuestDB.QuestDict['vsu4.1visitRoland'],
            QuestChoiceDNA(name='SpecialVisionSpell', questInt=4146,
                           giverId=NPCIds.ROLAND_RAGGART,
                           containers=(QuestDB.QuestDict['vsu4r1.1acquireGatorEyes'
                           ], QuestDB.QuestDict['vsu4r1.2acquireWasps'
                           ],
                           QuestDB.QuestDict['vsu4r1.3acquireScorpionEyes'
                           ], QuestDB.QuestDict['vsu4r1.4acquireBatEyes'
                           ])),
            QuestDB.QuestDict['vsu4.3acquireOrb'],
            QuestChoiceDNA(name='ExtractionSpell', questInt=4147,
                           giverId=NPCIds.ROLAND_RAGGART,
                           containers=(QuestDB.QuestDict['vsu4r2.1acquireSkeletonRibs'
                           ],
                           QuestDB.QuestDict['vsu4r2.2acquireNavyBadges'
                           ],
                           QuestDB.QuestDict['vsu4r2.3acquireScorpionStingers'
                           ],
                           QuestDB.QuestDict['vsu4r2.4acquireCrabShells'
                           ])),
            QuestChoiceDNA(name='FurtherExtraction', questInt=4148,
                           giverId=NPCIds.ROLAND_RAGGART,
                           containers=(QuestDB.QuestDict['vsu4r3.1acquireStumpBranch'
                           ],
                           QuestDB.QuestDict['vsu4r3.2acquireFlyTrapRoot'
                           ],
                           QuestDB.QuestDict['vsu4r3.3acquireWritsOfAuthority'
                           ],
                           QuestDB.QuestDict['vsu4r3.4acquireStrongerRibs'
                           ])),
            QuestDB.QuestDict['vsu4.5returnToRoland'],
            ),
        ),
    'spanish.ShipPVPBreadCrumbLadder': QuestLadderDNA(
        name='spanish.ShipPVPBreadCrumbLadder',
        questInt=27000,
        giverId=NPCIds.SPANISH_SHIPWRIGHT,
        firstQuestId='spanish.ShipPVPBreadCrumb',
        droppable=True,
        containers=(QuestDB.QuestDict['spanish.ShipPVPBreadCrumb'],
                    QuestDB.QuestDict['spanish.ShipPVPVisitLordA'],
                    QuestDB.QuestDict['spanish.ShipPVPFirstTrial'],
                    QuestDB.QuestDict['spanish.ShipPVPVisitLordB'],
                    QuestDB.QuestDict['spanish.ShipPVPSecondTrial']),
        ),
    'spanish.ShipPVPMainLadder': QuestLadderDNA(
        name='spanish.ShipPVPMainLadder',
        questInt=28000,
        giverId=NPCIds.GARCIA_DE_AVARCIA,
        firstQuestId='spanish.ShipPVPTaskA',
        droppable=True,
        containers=(
            QuestDB.QuestDict['spanish.ShipPVPTaskA'],
            QuestChoiceDNA(name='spanish.ShipPVPTaskB_C',
                           questInt=28001,
                           giverId=NPCIds.GARCIA_DE_AVARCIA,
                           containers=(QuestDB.QuestDict['spanish.ShipPVPTaskB'
                           ], QuestDB.QuestDict['spanish.ShipPVPTaskC'
                           ])),
            QuestDB.QuestDict['spanish.ShipPVPTaskF'],
            QuestDB.QuestDict['spanish.ShipPVPTaskG'],
            QuestChoiceDNA(name='spanish.ShipPVPTaskJ_K',
                           questInt=28003,
                           giverId=NPCIds.GARCIA_DE_AVARCIA,
                           containers=(QuestDB.QuestDict['spanish.ShipPVPTaskJ'
                           ], QuestDB.QuestDict['spanish.ShipPVPTaskK'
                           ])),
            QuestDB.QuestDict['spanish.ShipPVPTaskL'],
            QuestDB.QuestDict['spanish.ShipPVPTaskM'],
            QuestDB.QuestDict['spanish.ShipPVPTaskN'],
            QuestDB.QuestDict['spanish.ShipPVPTaskP'],
            ),
        ),
    'french.ShipPVPMainLadder': QuestLadderDNA(
        name='french.ShipPVPMainLadder',
        questInt=29000,
        giverId=NPCIds.PIERRE_LE_PORC,
        firstQuestId='french.ShipPVPTaskA',
        droppable=True,
        containers=(
            QuestDB.QuestDict['french.ShipPVPTaskA'],
            QuestChoiceDNA(name='french.ShipPVPTaskB_C',
                           questInt=29001,
                           giverId=NPCIds.PIERRE_LE_PORC,
                           containers=(QuestDB.QuestDict['french.ShipPVPTaskB'
                           ], QuestDB.QuestDict['french.ShipPVPTaskC'
                           ])),
            QuestDB.QuestDict['french.ShipPVPTaskF'],
            QuestDB.QuestDict['french.ShipPVPTaskG'],
            QuestChoiceDNA(name='french.ShipPVPTaskJ_K',
                           questInt=29003,
                           giverId=NPCIds.PIERRE_LE_PORC,
                           containers=(QuestDB.QuestDict['french.ShipPVPTaskJ'
                           ], QuestDB.QuestDict['french.ShipPVPTaskK'
                           ])),
            QuestDB.QuestDict['french.ShipPVPTaskL'],
            QuestDB.QuestDict['french.ShipPVPTaskM'],
            QuestDB.QuestDict['french.ShipPVPTaskN'],
            QuestDB.QuestDict['french.ShipPVPTaskP'],
            ),
        ),
    'om1.undeadFrenchSpanish': QuestLadderDNA(
        name='om1.undeadFrenchSpanish',
        questInt=30000,
        giverId=NPCIds.ORINDA,
        firstQuestId='om1.visitWoodruff',
        droppable=False,
        containers=(
            QuestDB.QuestDict['om1.visitWoodruff'],
            QuestDB.QuestDict['om1.defeatFrenchUndeadA'],
            QuestDB.QuestDict['om1.defeatFrenchUndeadB'],
            QuestDB.QuestDict['om1.defeatFrenchUndeadC'],
            QuestDB.QuestDict['om1.defeatFrenchUndeadD'],
            QuestChoiceDNA(name='om1.defeatSpanishUndead',
                           questInt=30010, giverId=NPCIds.WOODRUFF,
                           containers=(QuestDB.QuestDict['om1.defeatSpanishUndeadA'
                           ],
                           QuestDB.QuestDict['om1.defeatSpanishUndeadB'
                           ],
                           QuestDB.QuestDict['om1.defeatSpanishUndeadC'
                           ],
                           QuestDB.QuestDict['om1.defeatSpanishUndeadD'
                           ])),
            QuestDB.QuestDict['om1.defeatFrenchShipA'],
            QuestDB.QuestDict['om1.defeatFrenchShipB'],
            QuestDB.QuestDict['om1.defeatFrenchShipC'],
            QuestChoiceDNA(name='om1.defeatSpanishShips',
                           questInt=30014, giverId=NPCIds.WOODRUFF,
                           containers=(QuestDB.QuestDict['om1.defeatSpanishShipA'
                           ], QuestDB.QuestDict['om1.defeatSpanishShipB'
                           ], QuestDB.QuestDict['om1.defeatSpanishShipC'
                           ])),
            ),
        ),
    'FathersDay2008': QuestLadderDNA(
        name='FathersDay2008',
        questInt=10000,
        giverId=NPCIds.JACK_ROWDY_ROOSTER,
        droppable=True,
        firstQuestId='FathersDay2008.1visitGiladoga',
        containers=(QuestDB.QuestDict['FathersDay2008.1visitGiladoga'],
                    QuestChoiceDNA(name='FathersDay2008.2giladogaList',
                    questInt=10008, giverId=NPCIds.GILADOGA,
                    containers=(QuestDB.QuestDict['FathersDay2008t1.1RockCrabs'
                    ], QuestDB.QuestDict['FathersDay2008t1.2WitchDoctor'
                    ])),
                    QuestDB.QuestDict['FathersDay2008.3visitBronzeJohn'
                    ],
                    QuestDB.QuestDict['FathersDay2008t2.1bribeBronzeJohn'
                    ], QuestDB.QuestDict['FathersDay2008t4.1sinkShips'
                    ]),
        ),
    'OutfitQuestBasic': QuestLadderDNA(
        name='OutfitQuestBasic',
        questInt=30300,
        giverId=NPCIds.NATHANIEL_TRUEHOUND,
        droppable=False,
        firstQuestId='OQB.visitWilliamTurkA',
        containers=(
            QuestDB.QuestDict['OQB.visitWilliamTurkA'],
            QuestChoiceDNA(name='GamblingTasks', questInt=30301,
                           giverId=NPCIds.WILLIAM_TURK,
                           containers=(QuestDB.QuestDict['OQB.makeBlackjackMoney'
                           ], QuestDB.QuestDict['OQB.makePokerMoney'
                           ])),
            QuestChoiceDNA(name='GamblingByChallenge', questInt=30302,
                           giverId=NPCIds.WILLIAM_TURK,
                           containers=(QuestDB.QuestDict['OQB.challengingNavy'
                           ], QuestDB.QuestDict['OQB.challengingEITC'],
                           QuestDB.QuestDict['OQB.challengingNavyShips'
                           ],
                           QuestDB.QuestDict['OQB.challengingEITCShips'
                           ])),
            QuestDB.QuestDict['OQB.visitNathanielA'],
            QuestDB.QuestDict['OQB.visitWilliamTurkB'],
            QuestChoiceDNA(name='ErrandsForLuckyDeck', questInt=30303,
                           giverId=NPCIds.WILLIAM_TURK,
                           containers=(QuestDB.QuestDict['OQB.recoverFineRum'
                           ],
                           QuestDB.QuestDict['OQB.recoverBoneShavings'
                           ], QuestDB.QuestDict['OQB.recoverPrisonKey'
                           ])),
            QuestDB.QuestDict['OQB.deliverLuckyDeckToNathaniel'],
            QuestDB.QuestDict['OQB.visitWillTurnerA'],
            QuestDB.QuestDict['OQB.defeatNavyShips'],
            QuestChoiceDNA(name='WillFightTasks', questInt=30304,
                           giverId=NPCIds.WILL_TURNER,
                           containers=(QuestDB.QuestDict['OQB.defeatNavy'
                           ], QuestDB.QuestDict['OQB.defeatSkeleton'],
                           QuestDB.QuestDict['OQB.defeatEITC'])),
            QuestChoiceDNA(name='WillCreatureTasks', questInt=30305,
                           giverId=NPCIds.WILL_TURNER,
                           containers=(QuestDB.QuestDict['OQB.defeatAlligators'
                           ], QuestDB.QuestDict['OQB.defeatBats'],
                           QuestDB.QuestDict['OQB.defeatScorpions'],
                           QuestDB.QuestDict['OQB.defeatCrabs'],
                           QuestDB.QuestDict['OQB.defeatWasps'])),
            QuestDB.QuestDict['OQB.visitNathanielB'],
            QuestDB.QuestDict['OQB.visitEdwardShackleby'],
            QuestChoiceDNA(name='ExcentricTasks', questInt=30306,
                           giverId=NPCIds.EDWARD_SHACKLEBY,
                           containers=(QuestDB.QuestDict['OQB.retrieveAntiquePistol'
                           ], QuestDB.QuestDict['OQB.retrieveEITCManual'
                           ],
                           QuestDB.QuestDict['OQB.retrieveRareFeather'
                           ], QuestDB.QuestDict['OQB.retrieveCompass'
                           ])),
            QuestDB.QuestDict['OQB.visitNathanielC'],
            QuestDB.QuestDict['OQB.visitEdwardStormhawk'],
            QuestChoiceDNA(name='GarbageManTasks', questInt=30307,
                           giverId=NPCIds.EDWARD_STORMHAWK,
                           containers=(QuestDB.QuestDict['OQB.retrieveNavyShoeStrings'
                           ],
                           QuestDB.QuestDict['OQB.retrieveNavyAnchors'
                           ],
                           QuestDB.QuestDict['OQB.retrieveEITCParchment'
                           ],
                           QuestDB.QuestDict['OQB.retrieveEITCEmptyFlasks'
                           ])),
            QuestDB.QuestDict['OQB.visitNathanielD'],
            QuestDB.QuestDict['OQB.visitDarbyDryDock'],
            QuestChoiceDNA(name='ShipTasksA', questInt=30308,
                           giverId=NPCIds.DARBY_DRYDOCK,
                           containers=(QuestDB.QuestDict['OQB.retrievePlanksFromNavyShips'
                           ],
                           QuestDB.QuestDict['OQB.retrieveSailsFromEITCShips'
                           ],
                           QuestDB.QuestDict['OQB.retrieveWheelFromUndeadShips'
                           ])),
            QuestChoiceDNA(name='ShipTasksB', questInt=30309,
                           giverId=NPCIds.DARBY_DRYDOCK,
                           containers=(QuestDB.QuestDict['OQB.defeatEITCShipsB'
                           ], QuestDB.QuestDict['OQB.defeatNavyShipsB'
                           ])),
            QuestDB.QuestDict['OQB.visitNathanielE'],
            QuestChoiceDNA(name='PlunderingTasksA', questInt=30310,
                           giverId=NPCIds.NATHANIEL_TRUEHOUND,
                           containers=(QuestDB.QuestDict['OQB.retrieveClothFromNavyShip'
                           ],
                           QuestDB.QuestDict['OQB.retrieveCottonFromEITCShip'
                           ],
                           QuestDB.QuestDict['OQB.retrieveFabricFromNavyGuards'
                           ],
                           QuestDB.QuestDict['OQB.retrieveThreadFromUndead'
                           ],
                           QuestDB.QuestDict['OQB.retrieveCoinBagsFromEITCGuards'
                           ])),
            QuestDB.QuestDict['OQB.visitBartholomewWatkins'],
            QuestChoiceDNA(name='PlunderingTasksB', questInt=30311,
                           giverId=NPCIds.BARTHOLOMEW_WATKINS,
                           containers=(QuestDB.QuestDict['OQB.retrieveCursedSailClothFromUndead'
                           ],
                           QuestDB.QuestDict['OQB.retrieveBileFromScorpions'
                           ],
                           QuestDB.QuestDict['OQB.retrieveVenomFromWasps'
                           ],
                           QuestDB.QuestDict['OQB.retrieveBatGuanoFromBats'
                           ],
                           QuestDB.QuestDict['OQB.retrieveGatorSalivaFromGators'
                           ])),
            QuestDB.QuestDict['OQB.visitNathanielF'],
            ),
        ),
    'OutfitQuestIntermediate': QuestLadderDNA(
        name='OutfitQuestIntermediate',
        questInt=30100,
        giverId=NPCIds.AMELIA_SUNFELLOW,
        droppable=False,
        firstQuestId='OQI.visitIsaiah',
        containers=(
            QuestDB.QuestDict['OQI.visitIsaiah'],
            QuestChoiceDNA(name='OQI.recoverHatSupplies',
                           questInt=30104,
                           giverId=NPCIds.ISAIAH_CALLECUTTER,
                           containers=(QuestDB.QuestDict['OQI.recoverHides'
                           ],
                           QuestDB.QuestDict['OQI.recoverFlyTrapThread'
                           ])),
            QuestDB.QuestDict['OQI.visitJohnnyMcVane'],
            QuestChoiceDNA(name='OQI.winAtCards', questInt=30108,
                           giverId=NPCIds.JOHNNY_MCVANE,
                           containers=(QuestDB.QuestDict['OQI.playPoker'
                           ], QuestDB.QuestDict['OQI.playBlackjack'])),
            QuestDB.QuestDict['OQI.recoverRareFeathers'],
            QuestDB.QuestDict['OQI.visitAmeliaSunfellow'],
            QuestDB.QuestDict['OQI.visitBingham'],
            QuestDB.QuestDict['OQI.bribeBingham'],
            QuestChoiceDNA(name='EITCManifests', questInt=30115,
                           giverId=NPCIds.BINGHAM,
                           containers=(QuestDB.QuestDict['OQI.recoverManifests'
                           ], QuestDB.QuestDict['OQI.recoverBinghamsTip'
                           ])),
            QuestDB.QuestDict['OQI.deliverManifests'],
            QuestChoiceDNA(name='EITCShipments', questInt=30117,
                           giverId=NPCIds.AMELIA_SUNFELLOW,
                           containers=(QuestDB.QuestDict['OQI.recoverBoltsOfCloth'
                           ],
                           QuestDB.QuestDict['OQI.recoverFineScissors'
                           ], QuestDB.QuestDict['OQI.recoverSilkThread'
                           ])),
            QuestDB.QuestDict['OQI.returnIsaiah'],
            QuestDB.QuestDict['OQI.recoverNeedles'],
            QuestDB.QuestDict['OQI.visitScarlet'],
            QuestDB.QuestDict['OQI.bribeScarlet'],
            QuestChoiceDNA(name='ScarletsLetters', questInt=30138,
                           giverId=NPCIds.SCARLET,
                           containers=(QuestDB.QuestDict['OQI.scarletsLettersA'
                           ], QuestDB.QuestDict['OQI.scarletsLettersB'
                           ])),
            QuestChoiceDNA(name='ScarletsPearls', questInt=30132,
                           giverId=NPCIds.SCARLET,
                           containers=(QuestDB.QuestDict['OQI.recoverScarletsPearlA'
                           ],
                           QuestDB.QuestDict['OQI.recoverScarletsPearlB'
                           ],
                           QuestDB.QuestDict['OQI.recoverScarletsPearlC'
                           ],
                           QuestDB.QuestDict['OQI.recoverScarletsPearlD'
                           ],
                           QuestDB.QuestDict['OQI.recoverScarletsPearlE'
                           ])),
            QuestDB.QuestDict['OQI.returnIsaiahB'],
            QuestDB.QuestDict['OQI.visitBigPhil'],
            QuestChoiceDNA(name='PhilsAnimals', questInt=30137,
                           giverId=NPCIds.BIG_PHIL,
                           containers=(QuestDB.QuestDict['OQI.recoverChickensForPhil'
                           ], QuestDB.QuestDict['OQI.recoverPigsForPhil'
                           ])),
            QuestDB.QuestDict['OQI.returnIsaiahC'],
            QuestDB.QuestDict['OQI.visitAmeliaSunfellowB'],
            QuestDB.QuestDict['OQI.deliverCoinBag'],
            QuestDB.QuestDict['OQI.findJohnsStuff'],
            QuestChoiceDNA(name='WaspClearOut', questInt=30148,
                           giverId=NPCIds.JOHN_SMITH,
                           containers=(QuestDB.QuestDict['OQI.recoverWaspWings'
                           ], QuestDB.QuestDict['OQI.recoverWaspEggs'],
                           QuestDB.QuestDict['OQI.recoverWaspEssence'
                           ])),
            QuestChoiceDNA(name='CrabClearOut', questInt=30149,
                           giverId=NPCIds.JOHN_SMITH,
                           containers=(QuestDB.QuestDict['OQI.recoverCrabClaws'
                           ], QuestDB.QuestDict['OQI.recoverCrabShells'
                           ])),
            QuestDB.QuestDict['OQI.visitAmeliaSunfellowC'],
            QuestDB.QuestDict['OQI.recoverBeltBuckles'],
            QuestDB.QuestDict['OQI.returnIsaiahD'],
            QuestDB.QuestDict['OQI.recoverShoeDesigns'],
            QuestChoiceDNA(name='recoverMaterials', questInt=30154,
                           giverId=NPCIds.ISAIAH_CALLECUTTER,
                           containers=(QuestDB.QuestDict['OQI.recoverScorpionShells'
                           ],
                           QuestDB.QuestDict['OQI.recoverBoneShavings'
                           ],
                           QuestDB.QuestDict['OQI.recoverAlligatorHides'
                           ],
                           QuestDB.QuestDict['OQI.recoverVampireBatGuano'
                           ])),
            QuestDB.QuestDict['OQI.sinkEITCShips'],
            ),
        ),
    'OutfitQuestAdvanced': QuestLadderDNA(
        name='OutfitQuestAdvanced',
        questInt=30200,
        giverId=NPCIds.ADORIA_DOLORES,
        droppable=False,
        firstQuestId='OQA.visitRomanyBev',
        containers=(
            QuestDB.QuestDict['OQA.visitRomanyBev'],
            QuestDB.QuestDict['OQA.recoverShopApplication'],
            QuestDB.QuestDict['OQA.visitValentina'],
            QuestDB.QuestDict['OQA.defeatNavyGuards'],
            QuestDB.QuestDict['OQA.recoverCursedWood'],
            QuestDB.QuestDict['OQA.deliverChest'],
            QuestDB.QuestDict['OQA.visitValentinaC'],
            QuestDB.QuestDict['OQA.visitRomanyBevB'],
            QuestDB.QuestDict['OQA.deliverKrakenCloth'],
            QuestChoiceDNA(name='ShirtVestIngredientsA',
                           questInt=30208,
                           giverId=NPCIds.ADORIA_DOLORES,
                           containers=(QuestDB.QuestDict['OQA.recoverButtons'
                           ], QuestDB.QuestDict['OQA.recoverBoneDust'],
                           QuestDB.QuestDict['OQA.recoverHides'],
                           QuestDB.QuestDict['OQA.recoverCursedBark'
                           ])),
            QuestChoiceDNA(name='ShirtVestIngredientsB',
                           questInt=30213,
                           giverId=NPCIds.ADORIA_DOLORES,
                           containers=(QuestDB.QuestDict['OQA.recoverCursedCloth'
                           ],
                           QuestDB.QuestDict['OQA.recoverCursedThreads'
                           ])),
            QuestDB.QuestDict['OQA.recoverCursedNeedles'],
            QuestDB.QuestDict['OQA.visitValentinaB'],
            QuestDB.QuestDict['OQA.deliverVoodooArtifact'],
            QuestChoiceDNA(name='recoverVoodooArtifacts',
                           questInt=30221, giverId=NPCIds.ROMANY_BEV,
                           containers=(QuestDB.QuestDict['OQA.recoverVoodooArtifactsA'
                           ],
                           QuestDB.QuestDict['OQA.recoverVoodooArtifactsB'
                           ])),
            QuestDB.QuestDict['OQA.visitMaggieRigrage'],
            QuestChoiceDNA(name='recoverFamilyHeirloomsFromShips',
                           questInt=30226,
                           giverId=NPCIds.MAGGIE_RIGRAGE,
                           containers=(QuestDB.QuestDict['OQA.recoverFamilyHeirloomsA'
                           ],
                           QuestDB.QuestDict['OQA.recoverFamilyHeirloomsB'
                           ],
                           QuestDB.QuestDict['OQA.recoverFamilyHeirloomsC'
                           ])),
            QuestChoiceDNA(name='recoverFamilyHeirloomsFromLand',
                           questInt=30229,
                           giverId=NPCIds.MAGGIE_RIGRAGE,
                           containers=(QuestDB.QuestDict['OQA.recoverFamilyHeirloomsD'
                           ],
                           QuestDB.QuestDict['OQA.recoverFamilyHeirloomsE'
                           ])),
            QuestDB.QuestDict['OQA.visitRomanyBevC'],
            QuestDB.QuestDict['OQA.visitAdoriaDolores'],
            QuestDB.QuestDict['OQA.visitMorris'],
            QuestChoiceDNA(name='playCards', questInt=30235,
                           giverId=NPCIds.MORRIS,
                           containers=(QuestDB.QuestDict['OQA.playPoker'
                           ], QuestDB.QuestDict['OQA.playBlackjack'])),
            QuestDB.QuestDict['OQA.visitAdoriaDoloresB'],
            QuestDB.QuestDict['OQA.deliverRumBarrel'],
            QuestChoiceDNA(name='rumForGunner', questInt=30240,
                           giverId=NPCIds.GUNNER,
                           containers=(QuestDB.QuestDict['OQA.recoverRumBottles'
                           ], QuestDB.QuestDict['OQA.recoverRumBarrels'
                           ])),
            QuestDB.QuestDict['OQA.visitAdoriaDoloresC'],
            QuestDB.QuestDict['OQA.visitOlivier'],
            QuestChoiceDNA(name='remedyIngredients', questInt=30245,
                           giverId=NPCIds.OLIVIER,
                           containers=(QuestDB.QuestDict['OQA.recoverRottenMeat'
                           ],
                           QuestDB.QuestDict['OQA.recoverFlyTrapRoots'
                           ], QuestDB.QuestDict['OQA.recoverGatorSaliva'
                           ])),
            QuestDB.QuestDict['OQA.visitAdoriaDoloresD'],
            QuestDB.QuestDict['OQA.deliverCompass'],
            QuestDB.QuestDict['OQA.recoverLockgrimsLetter'],
            QuestChoiceDNA(name='GettingRevenge', questInt=30255,
                           giverId=NPCIds.DOG_LOCKGRIM,
                           containers=(QuestDB.QuestDict['OQA.defeatFlotsam'
                           ], QuestDB.QuestDict['OQA.defeatSpikeskull'
                           ], QuestDB.QuestDict['OQA.defeatKelpbrain'],
                           QuestDB.QuestDict['OQA.defeatBrinescum'])),
            QuestDB.QuestDict['OQA.visitAdoriaDoloresE'],
            QuestDB.QuestDict['OQA.recoverNavyChests'],
            QuestDB.QuestDict['OQA.recoverNavyChestKeys'],
            QuestDB.QuestDict['OQA.visitShochett'],
            QuestChoiceDNA(name='recoverTentacles', questInt=30264,
                           giverId=NPCIds.ADORIA_DOLORES,
                           containers=(QuestDB.QuestDict['OQA.recoverTentaclesA'
                           ], QuestDB.QuestDict['OQA.recoverTentaclesB'
                           ], QuestDB.QuestDict['OQA.recoverTentaclesC'
                           ],
                           QuestDB.QuestDict['OQA.recoverUrchinfistEye'
                           ])),
            QuestDB.QuestDict['OQA.deliverTentacles'],
            ),
        ),
    }
LaddersInitialized = False


def initializeLadders():
    print 'Initializing quest ladders...'
    for ladder in FameQuestLadderDict.values():
        ladder.initialize()

    for ladder in FortuneQuestLadderDict.values():
        ladder.initializeFortune(ladder.getDroppable())

    LaddersInitialized = True


if not LaddersInitialized:
    initializeLadders()


def getContainer(name):
    for ladder in FameQuestLadderDict.values():
        container = ladder.getContainer(name)
        if container:
            return container

    for ladder in FortuneQuestLadderDict.values():
        container = ladder.getContainer(name)
        if container:
            return container

    return None


def __getPath(node, path, name):
    if isinstance(node, QuestDNA):
        if node.getQuestId() == name:
            return (True, path)
        else:
            return (False, path)

    for ladder in node.getContainers():
        (found, path) = __getPath(ladder, path, name)
        if found:
            path.insert(0, ladder)
            return (found, path)

    return (False, path)


def getFamePath(name):
    path = []
    for ladder in FameQuestLadderDict.values():
        (found, path) = __getPath(ladder, path, name)
        if found:
            if ladder.getName() != 'MainStory':
                path.insert(0, ladder)
            return path

    return path


def getFortunePath(name):
    path = []
    for ladder in FortuneQuestLadderDict.values():
        (found, path) = __getPath(ladder, path, name)
        if found:
            path.insert(0, ladder)
            return path

    return path


def compileStats(name=None):
    questStatData = QuestStatData()
    if not name:
        for ladder in FameQuestLadderDict.values():
            ladder.compileStats(questStatData)

        for ladder in FortuneQuestLadderDict.values():
            ladder.compileStats(questStatData)

    ladder = getContainer(name)
    if ladder:
        ladder.compileStats(questStatData)
    print '========================================================='
    print questStatData
    print '========================================================='


def generateRogerFile(dict):
    for (key, quest) in dict.items():
        recGenerateRogerFile(quest)


def recGenerateRogerFile(ladder):
    print '{"%s", %s},' % (ladder.getQuestId(), ladder.getQuestInt())
    if ladder.isContainer():
        for container in ladder.containers:
            recGenerateRogerFile(container)
