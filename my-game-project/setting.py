from enum import Enum
from items import *

class WindowsSettings:
    name = 'Card battle revolution'
    width = 1500
    height = 900
    OutdoorScale = 2

class PlayerSettings:
    playerSpeed = 20
    playerWidth = 63.5
    playerHeight = 75
    playerHealth = 200
    playerAttack = 5
    PlayerDefense = 3
    PlayerMoves = 3

class NpcSettings:

    # 通用提示
    CommonSense = '''Your should response with less than 15 words.
    Here is some common sense you should know:
    1.This is a turn based card game named "card battle revolution" where players can counter their opponents by playing attack and defense cards.
    2.All resources,incluing health,attack,defense and moves,can be gained by purchasing in the NPC shop.The only way to gain resources is to defeat the NPCs for rewards.
    3.The health lost in battle will be restored after the end (regardless of success or failure).So don't worry about the health loss and try to defeat the NPCs.
    4.Each NPC has a unique dialogue system, and the player can talk with the NPC by pressing the "E" key.
    5.The player can move with the "WASD" keys.
    6.The player can fight with the NPC by pressing the "F" key.
    7.The player can purchase resources from the NPCs by pressing the "B" key.
    8.In each fight, the player can play a card to attack or defend by pressing "Q"and"E". The player can play up to 3 cards in each round initially.
    9.Some efficient tools can be purchased in the NPC shop to increase the number of cards played in each round.
    10.The player can press the "I" key to check the inventory and his current ability values.
    '''

    # Lilia 莉莉娅
    Task_Lilia = '''You are Lilia,a guiding NPC in a game world.You are sweet and kind-hearted.You like to eat sweet food.
    The player has just come to this world and needs your guidance.
    When the input involves about your identity or the setting of this game,
    you should tell him who you are and what you can do for him.
    '''+CommonSense
    dialogue1 = {"role": "system", "content":Task_Lilia}
    items1 = [("A worn-out helmet", 10), ("A worn-out armor", 20), ("A worn-out short sword", 30)]
    photopath1_1 = r".\assets\images\npc1.1.png"
    photopath1_2 = r".\assets\images\npc1.2.png"
    reward1 = 'The Lengendary Sword'
    currency1 = 100
    health1 = 50
    attack1 = 20
    Lilia = [dialogue1,items1,photopath1_1,photopath1_2,reward1,currency1,health1,attack1]

    #Berries 果酱
    Task_Berries = '''You are Berries, a merchant NPC in a game world.You are a little greedy and you like to tease the player.
    The player has just come to this world and needs your guidance.
    When the input involves about your identity or the setting of this game,
    you should tell him who you are and what you can do for him.
    '''+CommonSense
    dialogue2 = {"role": "system", "content":Task_Berries}
    items2 = [("Tears of the Dragon", 10), ("Dragon Soul", 20), ("Dragon bone", 30)]
    photopath2_1 = r".\assets\images\npc2.1.png"
    photopath2_2 = r".\assets\images\npc2.2.png"
    reward2 = 'The Lengendary Shield'
    currency2 = 100
    health2 = 50
    attack2 = 20
    Berries = [dialogue2,items2,photopath2_1,photopath2_2,reward2,currency2,health2,attack2]

    #Irin 璃音
    Task_Irin = '''You are Irin, a hostile NPC in a game world.You are evil and you are trying to make a scene.
    You are determined to stop the player here at any cost.
    When the input involves about your identity or the setting of this game,
    you should express your contemptuous attitude.
    '''+CommonSense 
    dialogue3 = {"role": "system", "content":Task_Irin}
    items3 = [("Undifined1", 999), ("Undifined2", 999), ("Undifined3", 999)]
    photopath3_1 = r".\assets\images\npc3.1.png"
    photopath3_2 = r".\assets\images\npc3.2.png"
    reward3 = 'The Evil Black Mandala'
    currency3 = 100
    health3 = 250
    attack3 = 40
    Irin = [dialogue3,items3,photopath3_1,photopath3_2,reward3,currency3,health3,attack3]
    
    #Sakura 樱
    Task_Sakura = '''You are Sakura,a NPC with senior status in a game world.
    You are wise and have a high level of combat power.
    You are afraid of the player's strength and want to test the player's strength.
    You want to see if the player is qualified to defeat the final boss.
    When the input involves about your identity or the setting of this game,
    you should persuade the player not to move forward anymore.
    '''+CommonSense
    dialogue4 = {"role": "system", "content":Task_Sakura}
    items4 = [("Undifined1", 999), ("Undifined2", 999), ("Undifined3", 999)]
    photopath4_1 = r".\assets\images\npc4.1.png"
    photopath4_2 = r".\assets\images\npc4.2.png"
    reward4 = "The philosopher's stone"
    currency4 = 100
    health4 = 700
    attack4 = 30
    Sakura = [dialogue4,items4,photopath4_1,photopath4_2,reward4,currency4,health4,attack4]

class SceneSettings:
    tileXnum = 120
    tileYnum = 72
    tileWidth = tileHeight = 25


class Gamepath:
    player = r".\assets\images\player.png"

    groundTiles = [
        r".\assets\tiles\grass12.png",
        r".\assets\tiles\grass13.png",
        r".\assets\tiles\grass14.png",
        r".\assets\tiles\grass15.png",
        r".\assets\tiles\grass16.png",
        r".\assets\tiles\grass17.png",
        r".\assets\tiles\grass18.png",
        r".\assets\tiles\grass19.png",
        r".\assets\tiles\grass20.png",
        r".\assets\tiles\grass21.png",
        r".\assets\tiles\grass22.png",
    ]

    tree = r".\assets\tiles\tree.png"

class Item_List:
#   物品名 = Items([攻击力,防御力,生命值,步数])
    The_Lengendary_Sword = Items([10,0,0,0],'A peerless sword in the world')
    The_Lengendary_Shield = Items([0,10,0,0],'A peerless shield in the world')
    A_worn_out_helmet = Items([0,1,0,0],"It's a bit worn out...But it can still be used")
    A_worn_out_armor = Items([0,0,2,0],"It's a bit worn out...But it can still be used")
    A_worn_out_short_sword = Items([3,0,0,0],"It's a bit worn out...But it can still be used")
    Tears_of_the_Dragon = Items([0,5,0,1],'Do you hear the dragon crying?')
    Dragon_Soul = Items([0,0,20,0],'The soul of the dragon')
    Dragon_bone = Items([4,0,10,0],'A bit horrible...Do you want to hear the story behind it?')
    items = {
        "The Lengendary Sword": The_Lengendary_Sword,
        "The Lengendary Shield": The_Lengendary_Shield,
        "A worn-out helmet": A_worn_out_helmet,
        "A worn-out armor": A_worn_out_armor,
        "A worn-out short sword": A_worn_out_short_sword,
        "Tears of the Dragon": Tears_of_the_Dragon,
        "Dragon Soul": Dragon_Soul,
        "Dragon bone": Dragon_bone,
    }
    keys = items.keys()