#!/usr/bin/python3

from models import storage
from models.event import Event
from models.dress import Dress
from models import storage_type
# import uuid

# events = [
#     'Birthday Party',
#     'Wedding Ceremony',
#     'Graduation Celebration',
#     'Corporate Conference',
#     'Music Concert',
#     'Sporting Event',
#     'Art Exhibition',
#     'Community Festival',
#     'Job Interview',
#     'Networking Mixer',
#     'Product Launch',
#     'Charity Fundraiser',
#     'Family Reunion',
#     'Educational Seminar',
#     'Fashion Show',
#     'Tech Hackathon',
#     'Film Premiere',
#     'Political Rally',
#     'Book Launch',
#     'Holiday Gathering',
#     'Cooking Class',
#     'Fitness Workshop',
#     'Science Fair',
#     'Theater Performance',
#     'Comedy Show',
#     'Travel Expo',
#     'Gaming Tournament',
#     'Poetry Slam',
#     'Dance Competition',
#     'Pet Adoption Event',
#     'Food Truck Festival',
#     'Gardening Workshop',
#     'Health and Wellness Fair',
#     'Photography Exhibition',
#     'Career Fair',
#     'Artisan Market',
#     'Car Show',
#     'Environmental Summit',
#     'Chess Tournament',
#     'Magic Show',
#     'Antique Fair',
#     'Radiothon',
#     'Astrology Workshop',
#     'DIY Craft Fair',
# ]

# # for event in events:
# #     event_dictionary = {"name": event}
# #     event_instance = Event(**event_dictionary)
# #     if storage_type == 'db':
# #         event_instance.save()


dresses_events = {
    "Formal Suit": ["Wedding Ceremony", "Graduation Celebration", "Corporate Conference"],
    "Business Casual": ["Job Interview", "Networking Mixer"],
    "Casual Jeans and T-Shirt": ["Birthday Party", "Music Concert", "Casual Chic"],
    "Athleisure": ["Sporting Event", "Fitness Workshop"],
    "Bohemian": ["Art Exhibition", "Music Concert"],
    "Vintage": ["Art Exhibition", "Vintage Rock"],
    "Smart Casual": ["Job Interview", "Educational Seminar"],
    "Hipster": ["Tech Hackathon", "Art Exhibition"],
    "Preppy": ["Community Festival", "Family Reunion"],
    "Gothic": ["Music Concert", "Halloween Party"],
    "Streetwear": ["Fashion Show", "Urban"],
    "Sportswear": ["Sporting Event", "Gaming Tournament"],
    "Boho-Chic": ["Fashion Show", "Artisan Market"],
    "Classic Elegant": ["Wedding Ceremony", "Formal Evening Gown"],
    "Retro": ["Art Exhibition", "Vintage Rock"],
    "Casual Chic": ["Casual Chic", "Casual Street Style"],
    "Punk": ["Music Concert", "Gaming Tournament"],
    "Minimalist": ["Art Exhibition", "Fashion Show"],
    "Tomboy": ["Sporting Event", "Casual Street Style"],
    "Festival Wear": ["Music Concert", "Community Festival"],
    "Urban": ["Fashion Show", "Artisan Market"],
    "Surfer Style": ["Summer Beachwear", "Gardening Workshop"],
    "Romantic": ["Wedding Ceremony", "Valentine's Day Dinner"],
    "Casual Shorts and Polo": ["Summer Beachwear", "Casual Chic"],
    "Western": ["Country Music Concert", "Western-themed Party"],
    "Business Formal": ["Corporate Conference", "Cocktail Attire"],
    "Cocktail Attire": ["Fashion Show", "Cocktail Party"],
    "Ethnic Traditional": ["Cultural Festival", "Wedding Ceremony"],
    "Glamorous Evening Wear": ["Gala Event", "Formal Evening Gown"],
    "Summer Beachwear": ["Summer Beach Party", "Travel Expo"],
    "Winter Cozy": ["Holiday Gathering", "Winter Fashion Show"],
    "Vintage Rock": ["Music Concert", "Vintage Rock Party"],
    "Edgy": ["Art Exhibition", "Music Concert"],
    "Country": ["Country Music Concert", "Western-themed Party"],
    "Artistic/Quirky": ["Art Exhibition", "DIY Craft Fair"],
    "Rugged Outdoor": ["Gardening Workshop", "Adventure Retreat"],
    "Nautical": ["Beach Party", "Sailing Event"],
    "Eclectic": ["Art Exhibition", "Fashion Show"],
    "Formal Evening Gown": ["Gala Event", "Formal Evening Party"],
    "Trendy High Fashion": ["Fashion Show", "High Fashion Event"],
    "Casual Street Style": ["Street Festival", "Casual Street Style"],
    "Laid-back Lounge": ["Casual Lounge Event", "Relaxation Retreat"],
    "Futuristic": ["Tech Hackathon", "Futuristic Art Exhibition"],
    "Sci-Fi Inspired": ["Sci-Fi Convention", "Movie Premiere"],
    "Uniform Style": ["Career Fair", "Military Ball"],
    "Funky Retro": ["Retro Party", "Vintage Market"],
}
dresses = storage.all(Dress)
for key, value in dresses_events.items():
    for dress in dresses.values():
        if key == dress.make_json().get('name'):
            for event in value:
                event_dict = {"name": event,
                              "dress_id": dress.id
                              }
                new_event = Event(**event_dict)
                new_event.save()

# event_dictionary = {"name": events[0],
#                     "dress_id" :"b1186a51-f294-4088-a989-94dbafe0b123"}
# event_instance = Event(**event_dictionary)
# event_instance.save()
