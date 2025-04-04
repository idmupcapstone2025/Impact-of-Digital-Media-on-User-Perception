import json
media_keywords = [
    "media",
    "advertising",
    "ad",
    "ads",
    "promotion",
    "marketing",
    "tv",
    "television",
    "radio",
    "newspaper",
    "magazine",
    "broadcast",
    "digital",
    "social",
    "social media",
    "content",
    "streaming",
    "video",
    "audio",
    "podcast",
    "blog",
    "press",
    "publicity",
    "banner",
    "billboard",
    "cinema",
    "commercial",
    "display",
    "google",
    "facebook",
    "instagram",
    "twitter",
    "linkedin",
    "youtube",
    "snapchat",
    "tiktok",
    "media buy",
    "impressions",
    "reach",
    "campaign",
    "sponsorship",
    "creative",
    "design",
    "production",
    "post-production",
    "animation",
    "graphics",
    "editorial",
    "shoot",
    "photography",
    "filming",
    "copywriting",
    "editing",
    "publishing",
    "distribution",
    "headline",
    "click-through",
    "CTR",
    "PPC",
    "CPC",
    "CPM",
    "media agency",
    "agency",
    "influencer",
    "endorsement",
    "affiliate",
    "SEO",
    "search engine",
    "web",
    "website",
    "newsletter",
    "email",
    "webinar",
    "event",
    "branding",
    "brand",
    "poster",
    "flyer",
    "outdoor",
    "OOH",
    "infographic",
    "storyboard",
    "voiceover",
    "jingle",
    "script",
    "broadcasting",
    "channel",
    "subscription",
    "media subscription",
    "platform",
    "editor",
    "host",
    "news",
    "headline",
    "screenshot",
    "promoted",
    "boost",
    "click",
    "media planning",
    "buying",
    "slot",
    "spot",
    "airtime",
    "placement",
    "native",
    "earned media",
    "owned media",
    "paid media",
    "outreach",
    "remarketing",
    "retargeting",
    "engagement",
    "metrics",
    "dashboard",
    "insights"
]
general_media_keywords = [
    "media", "advertising", "ad", "ads", "promotion", "marketing", "content", 
    "digital", "creative", "campaign", "distribution", "branding", "brand", 
    "publicity", "impressions", "reach", "agency", "media agency", 
    "media planning", "buying", "placement", "slot", "spot", "metrics", 
    "dashboard", "insights", "earned media", "owned media", "paid media", 
    "outreach", "remarketing", "retargeting", "engagement"
]

television_radio_keywords = [
    "tv", "television", "radio", "broadcast", "broadcasting", "channel", 
    "airtime", "commercial", "cinema", "spot", "script", "jingle", "voiceover"
]

print_media_keywords = [
    "newspaper", "magazine", "press", "editorial", "publishing", "headline", 
    "poster", "flyer", "infographic", "literature"
]

digital_media_keywords = [
    "social", "social media", "streaming", "video", "audio", "podcast", "blog", 
     "google", "facebook", "instagram", "twitter", "linkedin", "youtube", 
    "snapchat", "tiktok", "media buy", "click-through", "CTR", "PPC", "CPC", 
    "CPM", "SEO", "search engine", "web", "website", "newsletter", "email", 
    "webinar", "promoted", "boost", "click", "native", "platform"
]

outdoor_media_keywords = [
    "billboard", "outdoor", "OOH"
]

creative_production_keywords = [
    "design", "production", "post-production", "animation", "graphics", 
    "editorial", "shoot", "photography", "filming", "editing", "storyboard"
]

influencer_keywords = [
    "influencer", "endorsement", "affiliate"
]

software = [
    "Adobe", "Canva", "Final Cut", "editing", "creative suite"
]

categories = {
    "General": general_media_keywords,
    "Television/Radio": television_radio_keywords,
    "Print Media": print_media_keywords,
    "Digital Media": digital_media_keywords,
    "Outdoor Media": outdoor_media_keywords,
    "Creative Production": creative_production_keywords,
    "Influencer": influencer_keywords
}

def process1():
    palines=[]
    name="oppexp.txt"
    with open(name) as f:
        lines=f.readlines()
    for line in lines:
        parts=line.split("|")
        if(parts[10]=="PA"):
            print(line)
            palines.append(line)
    with open("FEC_CampaignFinanceData_PAonly.txt", "w") as f:
        for line in palines:
            f.write(line)
    return palines

def contains_media_keywords(text):
    text_lower=text.lower()
    return any(keyword.lower() in text_lower for keyword in media_keywords)

def process2():
    digital=[]
    print_media=[]
    general=[]
    creative=[]
    influence=[]
    software=[]
    outdoor=[]
    television=[]
    all_media=[]
    with open("FEC_CampaignFinanceData_PAonly.txt") as f:
        lines=f.readlines()
    for line in lines:
        splits=line.split("|")
        ''' The number "004" refers to: Advertising expenses -including
            general public political advertising (e.g., purchases of
            radio/television broadcast/cable time, print advertisements
            and related production costs)'''
        if (splits[16]=="004" or splits[16]=="102" or splits[16]=="103" or splits[16]=="105"):
            all_media.append(line)
            if any(word in splits[15].lower() for word in digital_media_keywords):
                digital.append(line)
            if any(word in splits[15].lower() for word in print_media_keywords):
                print_media.append(line)
            if any(word in splits[15].lower() for word in general_media_keywords):
                general.append(line)
            if any(word in splits[15].lower() for word in creative_production_keywords):
                creative.append(line)
            if any(word in splits[15].lower() for word in influencer_keywords):
                influence.append(line)
            if any(word in splits[15].lower() for word in software):
                software.append(line)
            if any(word in splits[15].lower() for word in outdoor_media_keywords):
                outdoor.append(line)
    with open("digital.txt", "w") as f:
        for line in digital:
            f.write(line)
    with open("print.txt", "w") as f:
        for line in print_media:
            f.write(line)
    with open("general.txt", "w") as f:
        for line in general:
            f.write(line)
    with open("creative.txt", "w") as f:
        for line in creative:
            f.write(line)
    with open("influence.txt", "w") as f:
        for line in influence:
            f.write(line)
    with open("software.txt", "w") as f:
        for line in software:
            f.write(line)
    with open("outdoor.txt", "w") as f:
        for line in outdoor:
            f.write(line)
    with open("all.txt", "w") as f:
        for line in all_media:
            f.write(line)

def read_dict_from_file(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
        # Safely evaluate the dictionary content
        dictionary = eval(content)
    return dictionary

def process3():
    candidate_committee={}
    with open('com2.csv') as f:
        lines=f.readlines()
        for line in lines:
            splits=line.split(',')
            for word in splits:
                if ("C0" in word) and ("{" not in line[-12:-3]):
                    candidate_committee[word]=line[-12:-3] #format is {committee id#, candidate id#}
    print(candidate_committee)
    json_string=json.dumps(candidate_committee)
    with open('committee:candidate.txt', 'w') as f:
        f.write(json_string)

def process4():
    candidate_committee=read_dict_from_file('committee:candidate.txt')
    candidate_purchases={}
    cand=None
    with open('all.txt') as f:
        lines=f.readlines()
        for line in lines:
            #try:
            comm=line[:9]
            try:
                cand=candidate_committee[comm] #get the candidate ID from the committee # of the purchase
            except:
                print(comm)
            try:
                purchases=candidate_purchases[cand] #get the current list of purchases from the purchases dictionary
            except:#if the candidate isn't currently in the array
                purchases=[]
            purchases.append(line) #add the current purchase (line) to the purchases array
            candidate_purchases.update({cand:purchases}) #add the updated purchases list back to candidate_purchases
        print(candidate_purchases)
        return candidate_purchases

class Candidate:
    idnum=0
    def __init__(self, idn):
        self.idnum=idn
        self.committees = []
        self.mediapurchases = []
    def addPurchase(self, purchase):
        self.mediapurchases.append(purchase)
    def addCommittee(self, comm):
        self.committees.append(comm)
    def getPurchases(self):
        return self.mediapurchases
    def getCommittees(self):
        return self.committees
    def __str__(self):
        return(str(self.idnum)+": Purchases: "+str(self.mediapurchases))



def getPAcandidates():
    candDict={}  #structure is committee:ID#
    paCands={}  #structure is ID#:Candidate object
    with open('committee_candidate.txt') as f:
        candDict=json.load(f)
        for comm in candDict:
            cand=candDict[comm]
            if(cand[2:4]=="PA"):
                #print(cand)
                if cand not in paCands:
                    new=Candidate(cand)
                    new.addCommittee(comm)
                    paCands[cand]=new
                else:
                    cur=paCands[cand]
                    cur.addCommittee(comm)
                    paCands[cand]=cur
    return paCands, candDict
def getPApurchases(paCands, candDict):
    unaffPur = []  # Purchases by committees not associated with candidates
    valid_codes = {"004", "102", "103", "105"}  # Valid codes for purchases

    with open('oppexp.txt') as f:
        lines = f.readlines()
        for line in lines:
            splits = line.split("|")
            try:
                # Ensure the committee ID exists in candDict
                if splits[0] not in candDict:
                    unaffPur.append(line)  # Committee not found, treat as unaffiliated
                    continue

                # Get candidate ID based on the committee
                candID = candDict[splits[0]]
                # Retrieve existing candidate
                cand = paCands[candID]
                # Check if purchase codes match the valid ones and associate the purchase
                if any(splits[i] in valid_codes for i in [16, 17, 18]):
                    cand.addPurchase(line)  # Add purchase to the correct candidate
            except IndexError:
                print(f"Malformed line skipped: {line.strip()}")
            except Exception as e:
                #print(f"Unexpected error: {e} for line: {line.strip()}")
                unaffPur.append(line)

        print(f"Unaffiliated purchases: {len(unaffPur)}")
    return paCands
    
            

if __name__=="__main__":
    #process2() #classifies purchases based on if they are media-based (not needed, found out how to classify them based on code)
    #process3() #produces a dictionary of {committee:candidate}
    '''purchases=process4()
    for x in purchases:
        print(x+":"+str(purchases[x]))
    print(len(purchases))
    with open("committee_candidate.txt") as f:
        f.seek(723808)
        char=f.read(1)
        char+=f.read(2)
        char+=f.read(3)
        char+=f.read(4)
        char+=f.read(5)
        char+=f.read(6)
        char+=f.read(7)
        char+=f.read(8)
        char+=f.read(9)
        print(char)'''
    paCands, candDict=getPAcandidates()
    paCands=getPApurchases(paCands, candDict)
    dictForFile={}
    for idnum, cand in paCands.items():
        purchases=cand.getPurchases()
        if len(purchases)!=0:
            #print(str(cand)+"\n")
            dictForFile[idnum]=purchases
    for idnum, purchases in dictForFile.items():
        totalSpent=0
        purposes=[]
        for purchase in purchases:
            parts=purchase.split('|')
            desc=parts[8] + ' ' + parts[15] + ' ' + parts[19]
            #print(desc)
            if (('FACEBOOK' in desc or 'FLEXPOINT MEDIA INC' in desc or 'RED MAVERICK MEDIA' in desc or 'TWITTER'
                    in desc or 'ADROLL' in desc or 'SQUARE SPACE' in desc or 'AMAZON' in desc or
                    'TEXT' in desc or 'CALLHUB.IO' in desc or 'PICTURE THIS' in desc or 'VOTERPING' in
                    desc or 'VOTER PING' in desc or 'JAMLOOP' in desc or 'MAILCHIMP' in desc or 'X ' in desc
                    or 'MAILERLITE' in desc or 'FIVERR' in desc or 'META' in desc or 'QR' in desc or
                    'DOMAIN' in desc or 'MR. MARKETING' in desc or 'MCSHANE LLC' in desc or 'SCHESINGER'
                    in desc or 'HEMLOCK' in desc or 'MARLIN' in desc or 'SMART MEDIA' in desc
                     or 'TARGETED VICTORY' in desc or 'FIFTH INFLUENCE' in desc or 'WBCB' in desc
                     or 'GOOGLE DIGITAL' in desc or 'TEXT REQUEST' in desc or 'BALUSTRADE' in desc) and 'button' not in desc):
                totalSpent+=float(parts[13])
                purposes.append(desc)
        print(idnum+': $'+str(totalSpent)+' on '+str(purposes))
    '''
    with open("paAdvertising.txt", "w") as f:
        f.write(str(dictForFile))
'''

            
