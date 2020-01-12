import random

ConferenceNames = ["10,000 Latkes", "24 Carrot Seven", "25,000 Mile Stones", "29 Psalms for 29 Palms",
                   "A Gathering of Hunters", "Act Out Your Age", "Adventure Camping", "Advertising Nauseum",
                   "Aesthetic Bug Gloss", "Air Fair", "Alanonymous", "Amagansett Go Around", "Amateur Barber Night",
                   "An Arbor Day to Remember", "Antisocial Darwinism", "Apathesis", "Apocalypso", "Aria Safari",
                   "Arise and Shinola", "Aromastotle", "Ass Texas", "Attila the Humm", "Aurora Tori Spelling",
                   "Away we golf", "Bali Who", "Balls of the Bull Festival", "Basking Bingo", "Beauteous Maximus",
                   "Bébé Boom", "Belch Blanket Babylon", "Belfascinating Rhythm", "Belfast United in Song",
                   "Bella Outdoors", "Below the Beltway", "Bible Quest", "Blog a Thong", "Blog-a-Thon", "Blueberry Jam",
                   "Bong-a-Thon", "Book Bound", "Book Trials", "Bora Bora Boar Hunt", "Boston Fantastic",
                   "Bowels and Whistles", "Brand Royalty", "Break a Peg Leg", "Bring Pluto Back!",
                   "Bring Your Boss Home From Work Day", "Bring Your Ex-Spouse to Work Day",
                   "Bring Your Mother-in-Law to Work Day", "Broncomania", "Brooklyn Bums Boogie the night away",
                   "Buffalo Roman", "Burn It On!", "Burn on the Fourth of July", "Bustin’ Britches Whiskeyfest",
                   "Buzzplosion", "Cabbage Training", "CactiDance", "Call it Green", "Camp Grandmada", "Campxotica",
                   "Candidate For a Day", "Candle Opera", "Candlelight Virgil", "Candy Candy!", "Career Cast",
                   "Caribbean Bottleneck", "Catholics and Protestants Untie", "Celebrity Palsy", "Centigrand",
                   "Chapter Elvis", "Cheering Larry", "Chewing Guam", "Chillennium", "Chiropractic Sojourn",
                   "Christmas PeaceFest 2001", "Christmas Together", "Circuitship", "CircusRodeo",
                   "Citroen to the Boen", "Club Hell Yea", "Coffee Dreamtime", "Coffee Rodeo", "Coffee RoundUp",
                   "Coffee Tsunami", "Coffee World", "Coffeebration", "Coffee-Go-Round", "Colony Clutch", "Comcentric",
                   "Condimantra", "Contortionist’s Training Camp", "Conundrum Grand", "Cookie Pagent",
                   "Corn Dog Social", "Corn Doggery", "Corn-Fed Beef Bowl", "Cosmetallic", "Coup de Veal",
                   "Coupe de Troupe", "Cubicide", "Cubicle Wars", "Dada Dwiddle", "Dancalicious", "Dance Contagion",
                   "Dance Fusion", "Dance Vibrations", "Dancellennium", "Danceweekly", "Darwin 911",
                   "Dawn of the Dead Festival", "Deep Blue Scene", "Deep Blue See", "Deliveranch",
                   "Demonstration Sunday", "Destination Destin", "Dial-A-Smile", "Digital Planet", "DIGITALPARTY.COM",
                   "Dog Country", "Dognost", "Dot Circus", "Dote", "Dotting the Eyes", "Drag Your Ass to Work Day",
                   "Dramantra", "Drawing Dead and Loving it", "Drinko de Mayo", "Dude Raunch", "Dutch Auction Rollover",
                   "e Me Up Scotty", "Ear Scorn", "Earfest.com", "Earth Cup", "Earth is Good Food", "Elderdrama",
                   "Emperor s R Us", "Eternity Waltz", "Event You All", "Existential Boy’s Night Out", "Exo Eccentric",
                   "Exo2000", "Exoblue", "ExoParty", "ExoPlanet", "Extinction Distinction", "Faire Moan",
                   "Far Away Feast", "Firebrand 500", "Firefly Friends Children’s Fund",
                   "Flaming Tongue Whiskey Suckoff", "Flannel Magic", "Flash em in the Pants", "FlyingRodeo",
                   "Foie Gras for Dummies", "Food for Feet", "Food Frolic", "Fork in the Roadkill", "Fornicon",
                   "Fornicult", "Forty Five Kids, Hot Dogs and Spaghetti", "Franchise Life", "Free Form Woe",
                   "Freudian Events", "Freud’s Follies", "Future Engineers of Canada", "Future Rodeo", "Geekola",
                   "GeekSeek", "Gems for Jesus", "GhandiFest", "Ginger Snapping", "Glace Lass",
                   "Gliding Lights Children’s Fund", "Glow Your Own", "Go for the Juggler", "Goon Boon", "GoTee",
                   "Greenclick", "Greenclicks", "Gretels and Goths", "Grill to Chill", "HaikuFest", "Halloween Howl",
                   "Hell 2Pay", "HipHop Hooray", "Hit the Good Books", "Hoist the Local Rag", "Home Plate Collection",
                   "Hoodie", "Hope Grows Fondler", "Howl Movement", "Hunter’s Gathering", "I Wood Knot No",
                   "Ice Cream Asocial", "Ice Cream Socialism", "Indian Summer", "Inhale Satan", "Inspire Choir",
                   "Interknack", "Internet Eternity", "Introducing the Inducing", "Jalapeño Fire Waltz",
                   "Jean Jacket Pool", "Jesus Drone", "Jesus Jive", "Jesus, Gandhi and Dan", "Jigging Sinatra",
                   "Jimmy Buffet’s Granola Fantasy Canteen", "Jumpstack", "Just Nuptials", "Just Say Know",
                   "Karma Farm", "Kibbles and Kitsch", "KidChat", "KidsOnly", "Kidstock", "Kimono Open", "Kinder Rock",
                   "Knit and Caboodle", "Know Show", "Knowledge World", "Lambastica", "Lands’ End of an Era",
                   "Le Petit Chef", "Let’s Talk Turducken!", "LightSpeed 3000", "Lingo Bingo", "Loco Motion",
                   "Loud and Queer", "Lovely Lovely Two", "LoveMusic", "LP Youth – Leadership Program for Youth",
                   "Lutheran Luau", "Mach Epoch", "Market de Sade", "Marmalade Parade", "Martha’s Rump Roast",
                   "Mattermind", "Miami Over Moon", "Mighty Millennium – A Bash for 2000", "Mississippi Moments",
                   "Mock Epoch", "Moon Boon", "Moonshine Wagon", "Motovate", "Motovation", "Moxi Biloxi", "MusiBlast",
                   "Mustang Mania", "Native ET", "Navel Grazing", "Neils Particle Board", "Neutron Bingo",
                   "New Whirled", "New York Punks Polka under the Planets", "Norse and Buggy", "Nude Attitude",
                   "NYAccord", "Objectify Your Future", "Occasion Alice", "Occasion Olly", "Of Corsica",
                   "Of Mice and Mein", "Oooh-Day", "Open Arms Kimono", "Open the Window", "OpenDoor",
                   "Origin of the Pisces", "Oy to the World", "Paintstorm", "Palms for Psalms", "Passive Fest",
                   "Pasta la Vista", "Peace by Peace", "Peace is Good Food", "Peace Love and Kitty Cats", "Peace Meal",
                   "Peace of Cake", "Peacemeal", "Pheno Barbie Doll", "Philidelphia Flux", "Pick up the Peaces",
                   "Pigeon Wednesday", "Pikachu and Hello Kitty Fight to the Death", "Pineapple Day", "Pipe Dreams",
                   "Piss Focus", "Planet Africa", "Plastic Fantastic", "Plastic Planet", "Poi Town & Country",
                   "Prawn Utopia", "Prawnscape", "Praying for Dollars", "Pride Aside", "Printo Supremo", "Printorama",
                   "PrintPlosion", "Project God", "Prothopedic", "Psychothon", "Quake Dance", "Quantifying Larry",
                   "Quatre-Vingts Morrison", "Rack Wars", "Raffle Your Feathers", "Raindance Ranch",
                   "Ranch Cross Dressing", "Rancho Merit", "Rap Doodle", "Reach for a Peace", "Reach For Peace",
                   "Ready Fortune Teller", "Reap the Mercury", "Retro Plum", "Retro Vile", "Retro-Yo", "Revering Paula",
                   "Ritual Wave", "Rock Okra", "Rogue Temptation", "Roman Candle Empire", "Sans Charo",
                   "Satelite Ranch", "Scrap Opera", "Screaming Tuesday", "Sequin", "Shock and Almonds", "Shock Talk",
                   "Shovel Up and Buck", "Sip and Shout", "Sisters and Blisters", "Slam Banjo", "Smart Ask",
                   "Smelt and a Smile", "Smokin’ the Data", "Smores and Greedy Ants", "Snow Lights", "So So Toboso",
                   "Solar Bingo", "Soma Night", "Soul You Know", "Soup Opera", "Speedbolt", "Spring-A-Ding",
                   "Spring-A-Ling", "SpringAlong", "SpringJam", "SpringSing", "Sprit of the Arts", "Steps Into Living",
                   "Stride for Life", "Striders on the Storm", "Striding Light", "Subterfuse", "Summer of Prawns",
                   "Super Ciao", "Survival of the Fattest", "Sympathy Slosh", "Tahoe a Go Go",
                   "Tall Tales and Nightingales", "Tango Latté", "Té Tango", "Teaming with Success", "Technoasis",
                   "Telethong", "Telluride Glide", "Tellurider", "That’s the Wrong Bong", "The Bakery Rave",
                   "The Buffoon Buffet", "The Feast or Famine", "The Great Bovine Picnic", "The Hermit Wars",
                   "The Hip Knows Therapy", "The Loop", "The Million Mime March", "The Monte Magum",
                   "The Nature of Nurture", "The New Abnormal", "The Point of Known Return",
                   "The Summit for Performance", "The World at Extra Large", "This Damn Planet", "Thong-a-Thon",
                   "Thread the Noodle", "Throng-a-Thon", "Tone Bone", "Tornado Picnic", "Tornado Rodeo", "Tres Huggers",
                   "Trinity Trona", "Trotting Ham Phallus", "Tunapocalypse", "Tussle In Tuscany",
                   "Tyrannosaurus Rocks!", "Uberlux", "Umpa Lava", "Virtual Rodeo", "Visionary Summit", "Vow Vagner",
                   "Wall Street on 100 Shares a Day", "Waltzing Meridian", "Waltzing with Eternity", "War on Peas",
                   "Wasabi Eating Contest", "Water Rodeo", "Watts Happening", "Weepers for Progress",
                   "Welcome Young Yankees", "Well2K", "Wellness 2000", "Wes World", "Wet the People", "Who’d a Thong?",
                   "Whoopie Birthday", "Why Hawaii?", "Why Solvang?", "Wig Week", "Wisdom Tooth Convention",
                   "Wise and in the Way", "Wit Knee Bisexual", "Wonka Renewal", "XORCat 5000", "Ye Old Neil Young",
                   "Yes Sir Rotisserie", "Yester Yore", "Yogasm", "YOU TURN - Leadership Program for Youth",
                   "Youth MP – Mentorship Program for Youth", "YouthZest", "Yucatango"]
ConferenceTypes = ["Scientific", "Business", "Multilingual", "Media", "Entertainment"]


def main():
    f = open("ConferencesAndConferenceDaysGeneratedExec.sql", "w")
    for x in range(70):
        conference_id = x
        conference_name = random.choice(ConferenceNames)
        day_of_month = random.randint(1, 20)

        start_date = "20" + str(random.randint(16, 21)) + "-" + str(random.randint(1, 12)).zfill(2) + "-" + str(
            day_of_month).zfill(2)
        days_amount = str(random.randint(3, 7))
        conference_type = random.choice(ConferenceTypes)
        building_id = str(random.randint(1, 50))
        organizer_id = str(random.randint(1, 50))
        customer_id = str(random.randint(1, 70))
        f.write(
            "EXEC AddConference @ConferenceName =\'" + conference_name + "\', @StartDate =\'" + start_date +
            "\', @DaysAmount =" + days_amount + ", @ConferenceType =\'" + conference_type +
            "\', @BuildingID =" + building_id + ", @OrganizerID =" + organizer_id +
            ", @CustomerID =" + customer_id+"\n")

        for y in range(int(days_amount)):
            # conference_day_id = str(x + y)
            day_number = str(y)
            participant_limit = str(random.randint(30, 200))
            date = start_date[:8] + str(int(start_date[-2:]) + y)
            f.write(
                "\tEXEC AddConferenceDay @DayNumber = " + day_number + ", @ParticipantLimit = " + participant_limit +
                ", @Date = \'" + date + "\', @ConferenceID = " + str(conference_id)+"\n")
    f.close()


if __name__ == "__main__":
    main()