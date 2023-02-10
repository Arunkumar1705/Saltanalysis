class radicals:
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

    def __init__(self, basic_radical, acid_radical):
        self.acid_radical = acid_radical
        self.basic_radical = basic_radical

    def Dry_Testtube_Heating(self):

        """ This test gives us the results for `carbonate` `nitrate` , 'nitrite'
        """
        if self.acid_radical.lower() == 'carbonate':

            Procedure1 = ' Salt is taken in a dry test tube  and is heated strongly.'
            Observation1 = 'A gas is evolved which turns lime water milky \n and extinguishes a lighted matchstick.'
            Conclusion1 = 'May be carbonate '

            return {'Dry test tube heating': [Procedure1, Observation1, Conclusion1]}

        elif self.acid_radical.lower() == 'nitrate':

            Procedure1 = ' Salt is taken in a dry test tube and is heated strongly.'
            Observation1 = ' Brown fumes of NO2 gas with the evolution of a gas \n which relights the glowing splinter'.translate(radicals.SUB)
            Conclusion1 = ' May be nitrate'

            return {'Dry test tube heating': [Procedure1, Observation1, Conclusion1]}

        elif self.acid_radical.lower() == 'nitrite':

            Procedure1 = ' Salt is taken in a dry test tube and is heated strongly.'
            Procedure2 = 'Starch iodide paper is held at the mouth of tube'

            Observation1 = ' Pale brown fumes'
            Observation2 = 'Turns Blue'

            Conclusion1 = ' May be nitrite'
            Conclusion2 = 'Nitrite is confirmed'

            return {'Dry test tube heating': [[Procedure1, Observation1, Conclusion1],
                                              [Procedure2,Observation2,Conclusion2]]}

        else:

            Procedure = ' Salt is taken in a dry test tube \n and is heated strongly.'
            Observation = 'No gas is evolved'
            Conclusion = 'Carbonate and Nitrate are absent'

            return {'Dry test tube heating': [Procedure, Observation, Conclusion]}

    def Dil_HCl(self):

        """ This test gives us the results for `carbonate` `sulphite`
        `nitrite` `sulphide`
        """

        if self.acid_radical.lower() == 'carbonate':

            Procedure1 = ' To the salt dil. HCl is added'
            Observation1 = ' Brisk effervescence with \n evolution of a gas which turns lime water milky'
            Conclusion1 = 'Carbonate is confirmed'

            return {'Action of Dil. HCl': [Procedure1, Observation1, Conclusion1]}

        elif self.acid_radical.lower() == 'sulphite':

            Procedure1 = ' To the salt dil. HCl is added'
            Procedure2 = ' Evolved gas is passed through acidified K2Cr2O7'.translate(radicals.SUB)
            Procedure3 = 'Evolved gas is passed through acidified KMnO4 '.translate(radicals.SUB)
            Procedure4 = 'To the salt solution BaCl2 solution is added'

            Observation1 = 'Gas is evolved with a chocking smell'
            Observation2 = 'Solution turns green without turbidity'
            Observation3 = 'Solution turns clear and colourless'
            Observation4 = 'White precipitate readily soluble in dil. HCl'

            Conclusion1 = 'May be Sulphite'
            Conclusion2 = 'Sulphite is present'
            Conclusion3 = 'Sulphite is confirmed'
            Conclusion4 = 'Due to the formation of BaSO3 \n which is readily soluble in HCl dil.'

            return {'Action of Dil. HCl': [[Procedure1, Observation1, Conclusion1],
                                           [Procedure2, Observation2, Conclusion2],
                                           [Procedure3, Observation3, Conclusion3],
                                           [Procedure4,Observation4,Conclusion4]]}

        elif self.acid_radical.lower() == 'nitrite':

            Procedure1 = 'To the salt dil. HCl is added'
            Procedure2 = 'Starch iodide paper is held \n at the mouth of the test tube'

            Observation1 = 'Pale brown fumes'
            Observation2 = 'Turns Blue'

            Conclusion1 = 'May be nitrite'
            Conclusion2 = 'Nitrite is confirmed'

            return {'Action of Dil.HCl': [[Procedure1, Observation1, Conclusion1],
                                          [Procedure2, Observation2, Conclusion2]]}

        elif self.acid_radical.lower() == 'sulphide':

            Procedure1 = 'To the salt dil. HCl is added and heated'
            Procedure2 = 'Lead acetate paper is held at the mouth of the test tube'
            Procedure3 = 'to the salt dil. HCl is added \n and the gas evolved is passed through acidified\n K2Cr2O7'.translate(
                radicals.SUB)
            Procedure4 = 'to the salt dil. HCl is added \n and the gas evolved is passed through alkaline\n KMnO4'.translate(
                radicals.SUB)

            Observation1 = 'a gas is evolved with a rottenegg smell'
            Observation2 = 'turns black'
            Observation3 = 'turns green with turbidity'
            Observation4 = 'the solution turns colourless'

            Conclusion1 = 'H2S is the gas with the rotten egg smell, may be sulphide'
            Conclusion2 = 'Sulphide is confirmed'
            Conclusion3 = 'Sulphide is confirmed .\n the turbidity is due to deposition of sulphur'
            Conclusion4 = 'sulphide is confirmed'


            return {'Action of Dil. HCl': [[Procedure1, Observation1, Conclusion1],
                                           [Procedure2, Observation2, Conclusion2],
                                           [Procedure3, Observation3, Conclusion3],
                                           [Procedure4, Observation4, Conclusion4]]}

        else:

            Procedure = 'To the salt dil. HCl is added and heated'
            Observation = 'No change'
            Conclusion = 'Absence of carbonate,Sulphide,Sulphite,Nitrite'

            return {'Action of Dil. HCl': [Procedure, Observation, Conclusion]}

    def Conc_Sulphuric(self):

        """ This test gives us the results for `iodide` `bromide`
        `nitrate` `chloride`
        """

        if self.acid_radical.lower() == 'iodide':

            Procedure1 = 'to the salt con. H2SO4 is added and is heated'.translate(radicals.SUB)
            Observation1 = 'Violet Vapours'
            Conclusion1 = 'Due to liberation of iodine'

            return {'Action of Conc. H2SO4'.translate(radicals.SUB): [Procedure1, Observation1, Conclusion1]}

        elif self.acid_radical.lower() == 'nitrate':

            Procedure2 = 'to the salt con H2SO4 is added and \n heated strongly followed by Cu turnings'.translate(
                radicals.SUB)
            Observation2 = 'Pale brown fumes which turn deep brown \n on adding Cu turnings. the solution turns blue at the bottom of the flask'
            Conclusion2 = 'the solution turns bluish green \n due to formation ofcopper nitrate'

            return {'Action of Conc. H2SO4'.translate(radicals.SUB): [Procedure2, Observation2, Conclusion2]}

        elif self.acid_radical.lower() == 'bromide':

            Procedure1 = 'to the salt con. H2SO4 is added '.translate(radicals.SUB)
            Observation1 = 'Reddish brown fumes even before heating'
            Conclusion1 = 'May be bromide'

            return {'Action of Conc. H2SO4'.translate(radicals.SUB): [Procedure1, Observation1, Conclusion1]}

        elif self.acid_radical.lower() == 'chloride':

            Procedure1 = 'to the salt con H2SO4 is added'.translate(radicals.SUB)
            Procedure2 = 'A glass rod dipped in NH4OH is held at\n the mouth of the test tube.'.translate(radicals.SUB)
            Procedure3 = 'MnO2 is added to the above test tube and heated strongly'.translate(radicals.SUB)

            Observation1 = 'White fumes'
            Observation2 = 'Dense white fumes'
            Observation3 = 'Greenish yellow gas is evolved which turns\n moist starch iodide paper blue=-black'

            Conclusion1 = 'May be Chloride'
            Conclusion2 = 'Due to formation of NH4Cl'.translate(radicals.SUB)
            Conclusion3 = 'Chloride is confirmed'

            return {'Action of Conc. H2SO4'.translate(radicals.SUB): [[Procedure1, Observation1, Conclusion1],
                                                                      [Procedure2, Observation2, Conclusion2],
                                                                      [Procedure3, Observation3, Conclusion3]]}
        else:

            Procedure = 'To the salt con H2SO4 is added'.translate(radicals.SUB)
            Observation = 'No fumes were evolved'
            Conclusion = 'Absence of Flourine,Chlorine,Bromine,Iodine,Nitrate'

            return {'Action of Conc. H2SO4'.translate(radicals.SUB): [Procedure, Observation, Conclusion]}

    def Sulphate(self):

        """ This test gives us the results for `sulphate`
        """
        if self.acid_radical.lower() == 'sulphate':

            Procedure1 = 'Salt solution is acidified with \n dil. HCl boiled and BaCl2 solution is added'.translate(radicals.SUB)
            Observation1 = 'White precipitate is formed which \n is insoluble in con. HCl'
            Conclusion1 = 'Sulphate is confirmed'

            return {'Test for Sulphate': [Procedure1, Observation1, Conclusion1]}

        else:

            Procedure = 'Salt solution is acidified with \n  dil. HCl boiled and BaCl2 solution is added'.translate(radicals.SUB)
            Observation = 'No precipitate is formed'
            Conclusion = 'Absence of sulphate'

            return {'Test for Sulphate': [Procedure, Observation, Conclusion]}

    def Phosphate(self):

        """ This test gives us the results for `phosphate`
        """

        if self.acid_radical.lower() == 'phosphate':

            Procedure1 = 'to the salt conc. HNO3 is added and \n heated followed by ammonium molybdate'.translate(radicals.SUB)
            Procedure2 = 'To the salt solution few drops of \n dil. HNO3 is added followed by \n AgNO3 and NH4OH added \n dropwise'

            Observation1 = 'Canary Yellow precipitate'
            Observation2 = 'Yellow Ring in neutral layer'

            Conclusion1 = 'Phosphate is confirmed'
            Conclusion2 = 'Phosphate is confirmed'

            return {'Test for Phosphate': [[Procedure1, Observation1, Conclusion1],
                                          [Procedure2,Observation2,Conclusion2]]}
        else:

            Procedure = 'to the salt conc. HNO3 is added and \n heated followed by ammonium molybdate'.translate(radicals.SUB)
            Observation = 'no precipitate'
            Conclusion = 'absence of phosphate'

            return {'Test for Phosphate': [Procedure, Observation, Conclusion]}

    def Oxalate(self):

        """ This test gives us the results for `oxalate`
        """

        if self.acid_radical.lower() == 'oxalate':

            procedure1 = 'to the salt dil. H2SO4 is added and \n heated followed by KMnO4'.translate(radicals.SUB)
            procedure2 = 'to the salt CaCl2 solution is added'.translate(radicals.SUB)

            Observation1 = 'KMnO4 decolourises'.translate(radicals.SUB)
            Observation2 = 'White precipitate which is \n insoluble in Acetic Acid'

            Conclusion1 = 'Oxalate may be present'
            Conclusion2 = 'Calcium Oxalate is formed. Oxalate is confirmed'

            return {'Test for Oxalate': [[procedure1, Observation1, Conclusion1],
                                         [procedure2, Observation2, Conclusion2]]}
        else:

            Procedure = 'to the salt dil. H2SO4 is added and \n heated followed by KMnO4'.translate(radicals.SUB)
            Observation = 'KMnO4 is not decolourised'.translate(radicals.SUB)
            Conclusion = 'absence of Oxalate'

            return {'Test for Oxalate': [Procedure, Observation, Conclusion]}

    def Acetate(self):

        """ This test gives us the results for `acetate`
        """

        if self.acid_radical.lower() == 'acetate':
            Procedure1 = 'To the salt, dil. HCl is added and is heated'
            Procedure2 = 'To the salt conc. H2SO4 is added and \n heated followed by 2-3 ml of ethanol'.translate(radicals.SUB)

            Observation1 = 'Vinegar like smell'
            Observation2 = 'Pleasant smell'

            Conclusion1 = 'Acetate is confirmed'
            Conclusion2 = 'Esterification takes place resulting \n in the formation of ethyl acetate'

            return {'Test for acetate': [[Procedure1, Observation1, Conclusion1], [Procedure2, Observation2, Conclusion2]]}
        else:
            Procedure = 'To the salt,dil. HCl is added and is heated'
            Observation = 'Vinegar like smell'
            Conclusion = 'Acetate is confirmed'

            return {'Test for acetate': [Procedure, Observation, Conclusion]}

    def Ammonium(self):
        """ This test gives us the results for `ammonium`
        """
        if self.basic_radical.lower() == 'ammonium':
            Procedure1 = 'to the salt NaOH is added and is heated'
            Procedure2 = 'A glass rod dipped in conc. HCl is held \n at the mouth of the testube'
            Procedure3 = 'a red litmus paper is held at the mouth of the test tube'
            Procedure4 = 'to the above solution nesslers reagent is added'

            Observation1 = 'white fumes'
            Observation2 = 'ense white fumes'
            Observation3 = 'turns blue'
            Observation4 = 'turns brown'

            Conclusion1 = 'May be ammonium'
            Conclusion2 = 'ammonium is confirmed'
            Conclusion3 = 'ammonium is confirmed'
            Conclusion4 = ' ammonium is confirmed'

            return {'Test for Ammonium': [[Procedure1, Observation1, Conclusion1],
                                          [Procedure2, Observation2,
                                              Conclusion2],
                                          [Procedure3, Observation3,
                                              Conclusion3],
                                          [Procedure4, Observation4, Conclusion4]]}

    def Lead(self):
        """ This test gives us the results for `lead`
        """
        if self.basic_radical.lower() == 'lead':
            Procedure1 = 'The white precipiate of PbCl2 is dissolved in hot water and divided into two parts'
            Procedure2 = 'To the 1st part K2CrO4 is added'
            Procedure3 = 'To the 2nd part, potassium iodide - KI is added (heated and cooled too see yellow spangles) '

            Observation1 = ''
            Observation2 = 'Yellow precipitate of PbCrO4'
            Observation3 = 'Golden yellow spangles'

            Conclusion1 = ''
            Conclusion2 = 'Presence of Lead'
            Conclusion3 = 'Lead is confirmed'

            return {'Test for Lead': [[Procedure1, Observation1, Conclusion1],
                                      [Procedure2, Observation2,
                                          Conclusion2],
                                      [Procedure3, Observation3, Conclusion3]]}

    def Copper(self):
        """ This test gives us the results for `copper`
        """
        if self.basic_radical.lower() == 'copper':
            Procedure1 = 'The black Precipitate of CuS is heated with dil.HNO3 and excess of NH4OH'
            Procedure2 = 'Acetic acid is added to the above solution'
            Procedure3 = 'To the Above solution K4[Fe(CN)6] ia added '

            Observation1 = 'Deep blue colouration'
            Observation2 = 'Colour turns blue'
            Observation3 = 'Chocolate brown precipitate'

            Conclusion1 = 'Due to the formation of copper tetramium complex'
            Conclusion2 = 'Acetic acid removes ammonia from complex'
            Conclusion3 = 'Due to the formation of Cu2[Fe(CN)6]'

            return {'Test for Copper': [[Procedure1, Observation1, Conclusion1],
                                        [Procedure2, Observation2, Conclusion2], [
                Procedure3, Observation3, Conclusion3]
            ]}

    def Arsenic(self):
        """ This test gives us the results for `arsenic`
        """
        if self.basic_radical.lower() == 'arsenic':
            Procedure1 = 'The yellow precipitate of As2S3 is boiled with NaOH and few drops of con.HCl is added and heated'

            Observation1 = 'The yellow precipitate reappears'

            Conclusion1 = 'Due to the formation of As2S3\n As3+ is confirmed'

            return {'Test for Arsenic': [[Procedure1, Observation1, Conclusion1]
                                         ]}

    def Ferric(self):
        """ This test gives us the results for `ferric`
        """
        if self.basic_radical.lower() == 'ferric':
            Procedure1 = 'Brown precipitate of Fe(OH)3 is boiled with dil.HCl and the solution is divide into three parts'
            Procedure2 = 'To the first part Ammonium thiocyanate'
            Procedure3 = 'To the second part Pottasium Ferrocyanate is added '
            Procedure4 = 'To the third part potassium ferrocyanate is added'

            Observation1 = ' '
            Observation2 = 'Blood red colouration'
            Observation3 = 'Prussian blue colouration is formed'
            Observation4 = 'Brown colouration'

            Conclusion1 = ' '
            Conclusion2 = 'Fe3+ is present'
            Conclusion3 = 'Fe3+ is confirmed'
            Conclusion4 = 'Fe3+ is confirmed'

            return {'Test for Ferric': [[Procedure1, Observation1, Conclusion1],
                                        [Procedure2, Observation2, Conclusion2], [
                Procedure3, Observation3, Conclusion3],
                [Procedure4, Observation4, Conclusion4]
            ]}

    def Aluminium(self):
        """ This test gives us the results for `aluminium`
        """
        if self.basic_radical.lower() == 'aluminium':
            Procedure1 = 'The gelatinous white precipitate of Al(OH)3 is divide into three parts'
            Procedure2 = 'To the first part dil.HCl is added'
            Procedure3 = 'To the second part NaOH is added and heated'
            Procedure4 = 'To the above solution Ssturated solution of NH4Cl is added'
            Procedure5 = 'FLAME TEST Ther third part of Al(OH)3 is dissolved in few drops of Con.HNO3.Filter paper dipped in cobalt nitrate solution and then in test solution and shown in flame'

            Observation1 = ' '
            Observation2 = 'It dissolves'
            Observation3 = 'It dissolves completely'
            Observation4 = 'Gelatinous precipitate reappears'
            Observation5 = 'Blue colour at the edge of the filter paper [Ternalds Blue]'

            Conclusion1 = ' '
            Conclusion2 = 'Presence of Al3+ is confirmed'
            Conclusion3 = 'Al(OH)3 is amphoteric in nature'
            Conclusion4 = 'Al3+ is confirmed'
            Conclusion5 = 'Due to the formation of CoAl2O4[Cobalt Aluminate]'

            return {'Test for Aluminium': [[Procedure1, Observation1, Conclusion1],
                                           [Procedure2, Observation2, Conclusion2], [
                Procedure3, Observation3, Conclusion3],
                [Procedure4, Observation4, Conclusion4],
                [Procedure5, Observation5, Conclusion5]]}

    def Zinc(self):
        """ This test gives us the results for `zinc`
        """
        if self.basic_radical.lower() == 'zinc':
            Procedure1 = 'The white Precipitate of ZnS is dissolved in dil.HCl and and the solution is divided into two parts'
            Procedure2 = 'To the first part potassium ferrocyanate is added'
            Procedure3 = 'To the second part NaOH is added dropwise'
            Procedure4 = 'H2S is passed through the above solution'
            Procedure5 = 'the precipitate of ZnS is dissolved in con.HNO3.A filter paper dipped in cobalt nitrate solution and then in test solution an dshown in flame'

            Observation1 = ' '
            Observation2 = 'Bluish white precipitate'
            Observation3 = 'White precipitate is formed and is soluble in excess NaOH'
            Observation4 = 'White precipitate if formed'
            Observation5 = 'Green edged ash'

            Conclusion1 = ' '
            Conclusion2 = 'Due to the the formation of Zn2[Fe(CN)6]'
            Conclusion3 = 'Zn(OH)2 is formed followed by Na2ZnO2 . Zn(OH)2 is amphoteric in nature'
            Conclusion4 = 'Due to formation of ZnS'
            Conclusion5 = 'Zn2+ is confirmed'

            return {'Test for Zinc': [[Procedure1, Observation1, Conclusion1],
                                      [Procedure2, Observation2, Conclusion2], [
                Procedure3, Observation3, Conclusion3], [Procedure4, Observation4, Conclusion4],
                [Procedure5, Observation5, Conclusion5]
            ]}

    def Cobalt(self):
        """ This test gives us the results for `cobalt`
        """
        if self.basic_radical.lower() == 'cobalt':
            Procedure1 = 'The Black Precipiate of CoS is dissolve din minimal quantity of con.HNO3 and heated . NH4SCN is added followed bu amul alcohol and the test tube is shaken well'

            Observation1 = 'The alcoholic layer turns blue '

            Conclusion1 = 'Co2+ is confirmed'

            return {'Test for Cobalt': [[Procedure1, Observation1, Conclusion1]]}

    def Nickel(self):
        """ This test gives us the results for `nickel`
        """
        if self.basic_radical.lower() == 'nickel':
            Procedure1 = 'The black precipitate of NiS is dissolved in Aqua regia (3 parts of Con.HCl and 1 part of con.HNO3) A portion of it is taken and made distinctly alkaline with NH4OH and DMG is added'

            Observation1 = 'Rosy red Precipitate '

            Conclusion1 = 'Ni2+ is confirmed'

            return {'Test for Cobalt': [[Procedure1, Observation1, Conclusion1]]}

    def Manganese(self):
        """ This test gives us the results for `manganese`
        """
        if self.basic_radical.lower() == 'manganese':
            Procedure1 = 'The flesh coloured precipitate of MnS is dissolve din few drops of Dil.HCl and boiled to drive off H2S. Dil.HNO3 is added followed by sodium bismuthate[NaBiO3]'

            Observation1 = 'Purple colouration is formed (Pink)'

            Conclusion1 = 'Mn2+ is confirmed'

            return {'Test for Manganese': [[Procedure1, Observation1, Conclusion1]]}

    def Barium(self):
        """ This test gives us the results for `barium`
        """
        if self.basic_radical.lower() == 'barium':
            Procedure1 = 'The white precipitate of BaCO3 is dissolve din acetic acid to drive off CO2 .It is divided into 3 parts '
            Procedure2 = 'To the first part K2CrO4 is added'
            Procedure3 = 'To the second part Ammonium Sulphate is added'
            Procedure4 = 'To the third part Ammonium Oxalate is added'
            Procedure5 = 'FLAME TEST The salt is made into a paste with con.HCl which is taken in a glass rod and shown in the flame'

            Observation1 = ' '
            Observation2 = 'Yellow precipitate'
            Observation3 = 'White precipitate'
            Observation4 = 'White Precipitate'
            Observation5 = 'Apple green colour'

            Conclusion1 = ' '
            Conclusion2 = 'Ba2+ is confirmed'
            Conclusion3 = 'Ba2+ is confirmed'
            Conclusion4 = 'Ba2+ is confirmed'
            Conclusion5 = 'Ba2+ is confirmed'

            return {'Test for Barium': [[Procedure1, Observation1, Conclusion1],
                                        [Procedure2, Observation2, Conclusion2], [
                Procedure3, Observation3, Conclusion3], [Procedure4, Observation4, Conclusion4],
                [Procedure5, Observation5, Conclusion5]
            ]}

    def Strontium(self):
        """ This test gives us the results for `strontium`
        """
        if self.basic_radical.lower() == 'strontium':
            Procedure1 = 'The white precipitate of SrCO3 is dissolve din acetic acid to drive off CO2 .It is divided into 3 parts '
            Procedure2 = 'To the first part K2CrO4 is added'
            Procedure3 = 'To the second part Ammonium Sulphate is added'
            Procedure4 = 'To the third part Ammonium Oxalate is added'
            Procedure5 = 'FLAME TEST The salt is made into a paste with con.HCl which is taken in a glass rod and shown in the flame'

            Observation1 = ' '
            Observation2 = 'No precipitate'
            Observation3 = 'White precipitate'
            Observation4 = 'White Precipitate'
            Observation5 = 'Crimson red colour'

            Conclusion1 = ' '
            Conclusion2 = 'Sr2+ is absent'
            Conclusion3 = 'Presence of Sr2+'
            Conclusion4 = 'Presence of Sr2+ is confirmed'
            Conclusion5 = 'Sr2+ is confirmed'

            return {'Test for Strontium': [[Procedure1, Observation1, Conclusion1],
                                           [Procedure2, Observation2, Conclusion2], [
                Procedure3, Observation3, Conclusion3], [Procedure4, Observation4, Conclusion4],
                [Procedure5, Observation5, Conclusion5]
            ]}

    def Calcium(self):
        """ This test gives us the results for `calcium`
        """
        if self.basic_radical.lower() == 'calcium':
            Procedure1 = 'The white precipitate of SrCO3 is dissolve din acetic acid to drive off CO2 .It is divided into 3 parts '
            Procedure2 = 'To the first part K2CrO4 is added'
            Procedure3 = 'To the second part Ammonium Sulphate is added'
            Procedure4 = 'To the third part Ammonium Oxalate is added'
            Procedure5 = 'FLAME TEST The salt is made into a paste with con.HCl which is taken in a glass rod and shown in the flame'

            Observation1 = ' '
            Observation2 = 'No precipitate'
            Observation3 = 'No precipitate'
            Observation4 = 'White Precipitate'
            Observation5 = 'Brick red colour'

            Conclusion1 = ' '
            Conclusion2 = 'Ba2+ is absent'
            Conclusion3 = 'Absence of Sr2+ Ba2+'
            Conclusion4 = 'Presence of Ca2+ is confirmed'
            Conclusion5 = 'Ca2+ is confirmed'

            return {'Test for Calcium': [[Procedure1, Observation1, Conclusion1],
                                         [Procedure2, Observation2, Conclusion2], [
                Procedure3, Observation3, Conclusion3], [Procedure4, Observation4, Conclusion4],
                [Procedure5, Observation5, Conclusion5]
            ]}

    def Magnesium(self):
        """ This test gives us the results for `magnesium`
        """
        if self.basic_radical.lower() == 'magnesium':
            Procedure1 = 'To the filtrate of Group 5 Disodium hydrogrn phospate is added Na2HPO4'
            Procedure2 = 'To the above Precipitate con.HCl is added followed by Magnesson reagent and NaOH'

            Observation1 = 'White Precipitate'
            Observation2 = 'Blue Precipitate'

            Conclusion1 = 'Mg2+ is confirmed'
            Conclusion2 = 'Mg2+ is confirmed'

            return {'Test for Magnesium': [[Procedure1, Observation1, Conclusion1],
                                           [Procedure2, Observation2, Conclusion2]
                                           ]}


    def Special_Sulphide(self):
        if self.acid_radical.lower() == 'sulphide':
            Procedure5 = 'To the salt sodium nitro prusside is added'
            Observation5 = 'Purlple Colouration'
            Conclusion5 = 'Sulphide is confirmed'

            return {'Special Test for Sulphide': [Procedure5, Observation5, Conclusion5]}
        else:
            pass

    def Special_Nitrite(self):
        if self.acid_radical.lower() == 'nitrite':
            Procedure3 = 'To the salt dil. H2SO4 is added followed by KMnO4'.translate(
                radicals.SUB)
            Observation3 = 'Solution becomes colourless'
            Conclusion3 = 'Nitrite is confirmed'

            return{'Special Test for Nitrite': [Procedure3, Observation3, Conclusion3]}

        else:
            pass

    def Special_Acetate(self):
        if self.acid_radical.lower() == 'acetate':
            Procedure3 = 'To the salt sol. FeCL3 is added '.translate(
                radicals.SUB)
            Procedure4 = 'The solution is diluted and is boiled'
            Procedure5 = 'Dilute HCl is added to the above test tube'

            Observation3 = 'Deep red coluration'
            Observation4 = 'Precipitate is formed'
            Observation5 = 'Solution turns colourless'

            Conclusion3 = 'Acetate is confirmed'
            Conclusion4 = 'Due to the formation of Ferric Acetate'
            Conclusion5 = 'Acetate is confirmed'

            return {'Special test for acetate': [[Procedure3, Observation3, Conclusion3], [Procedure4, Observation4, Conclusion4],
                                                 [Procedure5, Observation5, Conclusion5]]}
        else:
            pass

    def Wet_Chloride(self):
        if self.acid_radical.lower() == 'chloride':
            Procedure4 = 'Salt is mixed with K2Cr2O7 and \n conc. H2SO4 and is heated strongly'.translate(
                radicals.SUB)
            Procedure5 = 'The gas is passed through NaOH solution \n and Lead acetate is added '

            Observation4 = 'Reddish brown fumes'
            Observation5 = 'Yellow precipitate'

            Conclusion4 = 'Due to formation of Cromyl Chloride'
            Conclusion5 = 'Due to formation of lead chromate'

            return {'Chromyl Chloride Test': [[Procedure4, Observation4, Conclusion4], [Procedure5, Observation5, Conclusion5]]}

        else:
            pass

    def Wet_Halides(self):
        if self.acid_radical.lower() in ['chloride','bromide','iodide']:
            Procedure = 'To the salt solution dilute \n HNO3 is added followed by \n AgNO3'
            if self.acid_radical.lower() == 'chloride':

                Observation = 'Curdly white ppt \n readily soluble in NH4OH'
            elif self.acid_radical.lower() == 'bromide':
                Observation = 'Pale yellow ppt \n difficult to  soluble in NH4OH'
            else:
                Observation = 'Deep yellow ppt \n insoluble in NH4OH'

            Conclusion = 'Due to the formation of nitrosyl \n ferrous sulphate, brown ring \n is formed'

            return {'Wet tests of Halides':[Procedure,Observation,Conclusion]}
        else:
            Procedure = 'To the salt solution dilute \n HNO3 is added followed by \n AgNO3'
            Observation = 'no precipitate'
            Conclusion = 'Absence of halides'

            return {'Wet tests of Halides': [Procedure, Observation, Conclusion]}

    def Wet_Nitrate(self):
        if self.acid_radical.lower() == 'nitrate':
            Procedure = 'To the salt solution dilute \n H2SO4 is addded followed by \n freshly prepared saturated \
            solution of FeSO4.\n '
            Observation = 'Brown ring appears at the junction of \n aqueous and acid layer'
            Conclusion = 'Due to the formation of nitrosyl \n ferrous sulphate, brown ring \n is formed'

            return {'Wet test of Nitrite': [Procedure, Observation, Conclusion]}
        else:
            Procedure = 'To the salt solution dilute \n H2SO4 is addded followed by \n freshly prepared saturated \
                        solution of FeSO4.\n '
            Observation = 'No brown ring'
            Conclusion = 'Nitrite is absent'

            return {'Wet test of Nitrite': [Procedure, Observation, Conclusion]}

    def Wet_Sulphate(self):
        if self.acid_radical.lower()=='sulphate':
            Procedure = 'To the salt solution acetic acid is added \n followed by lead acetate'
            Observation = 'White Precipitate of \n PbSO4'
            Conclusion = 'Sulphate is confirmed'
            return {'Wet tests of Sulphates': [Procedure, Observation, Conclusion]}
        else:
            Procedure = 'To the salt solution acetic acid is added \n followed by lead acetate'
            Observation = 'No white Precipitate'
            Conclusion = 'Sulphate is absent'
            return {'Wet tests of Sulphate': [Procedure, Observation, Conclusion]}