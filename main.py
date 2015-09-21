def main():

    character = Character()

    print '======================================================================='
    print 'Welcome to Rush\'s Dungeons & Dragons (5th Edition) Character Creator!!'
    print '======================================================================='
    print
    print
    print '=============='
    print 'Race Selection'
    print '=============='
    print
    RaceMenu(character)


def RaceMenu(character):
    print 'Here\'s the list of races. Select the number of the one you\'d like to be'
    print '1 - Dwarf'
    print '2 - Elf'
    print '3 - Halfling'
    print '4 - Human'
    print '5 - Dragonborn'
    print '6 - Gnome'
    print '7 - Half-Elf'
    print '8 - Half-Orc'
    print '9 - Tiefling'

    menuChoice = input('Selection: ')

    if menuChoice > 0 and menuChoice < 10:
        if menuChoice == 1:
            SetDwarf(character)
        elif menuChoice == 2:
            SetElf(character)
        elif menuChoice == 3:
            SetHalfling()
        elif menuChoice == 4:
            SetHuman()
        elif menuChoice == 5:
            SetDragonborn()
        elif menuChoice == 6:
            SetGnome()
        elif menuChoice == 7:
            SetHalfElf()
        elif menuChoice == 8:
            SetHalfOrc()
        else:
            SetTiefling()
    else:
        print 'Invalid menu choice'
        RaceMenu()

    character.dumpInfo()


def SetDwarf(character):

    character.Race = 'Dwarf'
    character.ChaInc += 2
    character.Size = 'Medium'
    character.speed = 25
    character.Traits.append('Heavy armor movement penalty removed')
    character.Traits.append('Darkvision')
    character.Traits.append('Dwarven Resilience')
    character.Traits.append('Stonecunning')
    character.Languages.append('Common')
    character.Languages.append('Dwarvish')
    character.WeaponProficiencies.append('Battleaxe')
    character.WeaponProficiencies.append('Handaxe')
    character.WeaponProficiencies.append('Light Hammer')
    character.WeaponProficiencies.append('Warhammer')

    print
    print 'Choose your subrace'
    print '1 - Hill Dwarf'
    print '2 - Mountain Dwarf'

    menuChoice = input('Selection: ')

    if menuChoice == 1:
        character.Subrace = 'Hill Dwarf'
        character.WisInc += 1
        character.Traits.append('Dwarven Toughness')
    elif menuChoice == 2:
        character.Subrace = 'Mountain Dwarf'
        character.StrInc += 2
        character.Traits.append('Dwarven Armor Training')
        character.ArmorProficiencies.append('Light')
        character.ArmorProficiencies.append('Medium')
    else:
        print 'Invalid menu choice'
        print
        SetDwarf()

    return


def SetElf(character):

    character.Race = 'Elf'
    character.DexInc += 2
    character.Size = 'Medium'
    character.speed = 30
    character.Traits.append('Trance')
    character.Traits.append('Darkvision')
    character.Traits.append('Fey Ancestry')
    character.Traits.append('Keen Senses')
    character.SkillProficiencies.append('Perception')
    character.Languages.append('Common')
    character.Languages.append('Elvish')

    print 'Choose your subrace'
    print '1 - High Elf'
    print '2 - Wild Elf'
    print '3 - Drow (consult your DM)'

    menuChoice = input('Selection: ')

    if menuChoice == 1:
        character.Subrace = 'High Elf'
        character.IntInc += 1
        character.Traits.append('Elf Weapon Training')
        character.WeaponProficiencies.append('Longsword')
        character.WeaponProficiencies.append('Shortsword')
        character.WeaponProficiencies.append('Shortbow')
        character.WeaponProficiencies.append('Longbow')
    elif menuChoice == 2:
        character.Subrace = 'Wild Elf'
        character.WisInc += 1
        character.Traits.append('Elf Weapon Training')
        character.WeaponProficiencies.append('Longsword')
        character.WeaponProficiencies.append('Shortsword')
        character.WeaponProficiencies.append('Shortbow')
        character.WeaponProficiencies.append('Longbow')
        character.Traits.append('Fleet of Foot')
        character.speed = 35
        character.Traits.append('Mask of the Wild')
    elif menuChoice == 3:
        character.Subrace = 'Drow'
        character.ChaInc += 1
        character.Traits.append('Superior Darkvision')
        character.Traits.append('Sunlight Sensitivity')
        character.Traits.append('Drow Magic')
        character.Traits.append('Drow Weapon Training')
        character.WeaponProficiencies.append('Rapier')
        character.WeaponProficiencies.append('Shortsword')
        character.WeaponProficiencies.append('Hand Crossbow')
    else:
        print 'Invalid menu choice'
        print
        SetElf()

    return


class Character():
    Race = 'Default'
    Subrace = 'Default'
    Str = 10
    StrInc = 0
    Dex = 10
    DexInc = 0
    Con = 10
    ConInc = 0
    Int = 10
    IntInc = 0
    Wis = 10
    WisInc = 0
    Cha = 10
    ChaInc = 0
    Traits = []
    Languages = []
    WeaponProficiencies = []
    ArmorProficiencies = []
    SkillProficiencies = []


    def dumpInfo(self):
        print self.Race
        print self.Subrace
        print self.Str
        print self.StrInc
        print self.Dex
        print self.DexInc
        print self.Con
        print self.ConInc
        print self.Int
        print self.IntInc
        print self.Wis
        print self.WisInc
        print self.Cha
        print self.ChaInc
        print self.Traits
        print self.Languages
        print self.WeaponProficiencies
        print self.ArmorProficiencies
        print self.SkillProficiencies

if __name__ == '__main__':
    main()