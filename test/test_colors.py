from collections import Counter
from ast import literal_eval
import matplotlib.pyplot as plt

dict_countrycode2info={
"AND": ["1", "Andorra", "AND", "Latin", "1004", "01-06-2018-22-09-2018", "PAPI", "Catalan,English,Spanish,French"],
"ARG": ["2", "Argentina", "ARG", "Latin", "1003", "04-07-2017-19-07-2017", "PAPI", "Spanish"],
"ARM": ["4", "Armenia", "ARM", "Isolate", "1223", "07-05-2021-07-06-2021", "CAPI", "Armenian"],
"AUS": ["3", "Australia", "AUS", "Anglosphere", "1813", "06-04-2018-06-08-2018", "Mail/Post", "English"],
"BGD": ["5", "Bangladesh", "BGD", "Indo-Iranian", "1200", "03-12-2018-24-12-2018", "PAPI", "Bengali"],
"BOL": ["6", "Bolivia", "BOL", "Latin", "2067", "18-01-2017-07-03-2017", "CAPI", "Spanish"],
"BRA": ["7", "Brazil", "BRA", "Latin", "1762", "15-05-2018-11-06-2018", "CAPI", "Portuguese"],
"CAN": ["8", "Canada", "CAN", "Anglosphere", "4018", "02-10-2020-19-10-2020", "CAWI", "English,French"],
"CDE": ["65", "Canada_English", "CDE", "Anglosphere", "0", "11-02-2020-23-03-2020", "CAPI", "English"],
"CDF": ["66", "Canada_French", "CDF", "Latin", "0", "11-02-2020-23-03-2020", "CAPI", "French"],
"CHL": ["9", "Chile", "CHL", "Latin", "1000", "06-01-2018-05-02-2018", "CAPI", "Spanish"],
"CHN": ["10", "China", "CHN", "EastAsia", "3036", "07-07-2018-12-10-2018", "PAPI", "Chinese"],
"COL": ["11", "Colombia", "COL", "Latin", "1520", "30-11-2018-22-12-2018", "CAPI", "Spanish"],
"CYP": ["12", "Cyprus", "CYP", "Isolate", "1000", "13-05-2019-04-06-2019", "PAPI", "Greek,Turkish"],
"CZE": ["13", "Czechia", "CZE", "Slavic", "1200", "11-02-2022-13-05-2022", "CAPI", "Czech"],
"DEU": ["17", "Germany", "DEU", "Germanic", "1528", "25-10-2017-31-03-2018", "CAPI", "German"],
"ECU": ["14", "Ecuador", "ECU", "Latin", "1200", "24-01-2018-03-03-2018", "CAPI", "Spanish"],
"EGY": ["15", "Egypt", "EGY", "Semetic", "1200", "22-06-2018-07-07-2018", "CAPI", "Arabic"],
"ETH": ["16", "Ethiopia", "ETH", "Semetic", "1230", "06-02-2020-19-03-2020", "CAPI", "Amharic,Oromo,Tigris"],
"GBR": ["19", "Great_Britain", "GBR", "Anglosphere", "2609", "02-03-2022-07-09-2022", "CAPI/CAWI/Post/Video_interviewing", "English"],
"GRC": ["18", "Greece", "GRC", "Isolate", "1200", "08-09-2017-16-10-2017", "PAPI", "Greek"],
"GTM": ["20", "Guatemala", "GTM", "Latin", "1203", "03-10-2019-25-02-2020", "CAPI", "Spanish"],
"HKG": ["21", "Hong_Kong_SAR", "HKG", "EastAsia", "2075", "16-07-2018-11-11-2018", "PAPI/CAWI", "Cantonese,English,Putonghua"],
"IDN": ["22", "Indonesia", "IDN", "EastAsia", "3200", "01-06-2018-20-08-2018", "CAPI", "Indonesian"],
"IRN": ["23", "Iran", "IRN", "Indo-Iranian", "1499", "24-03-2020-17-04-2020", "PAPI", "Persian"],
"IRQ": ["24", "Iraq", "IRQ", "Semetic", "1200", "08-06-2018-28-06-2018", "CAPI/PAPI", "Arabic"],
"JOR": ["26", "Jordan", "JOR", "Semetic", "1203", "07-06-2018-14-06-2018", "CAPI", "Arabic"],
"JPN": ["25", "Japan", "JPN", "EastAsia", "1353", "05-09-2019-26-09-2019", "Mail/Post", "Japanese"],
"KAZ": ["27", "Kazakhstan", "KAZ", "Turkic", "1276", "01-10-2018-30-11-2018", "PAPI", "Kazakh,Russian"],
"KEN": ["28", "Kenya", "KEN", "SubSaharanAfrica", "1266", "22-05-2021-22-06-2022", "CAPI", "Swahili"],
"KGZ": ["29", "Kyrgyzstan", "KGZ", "Turkic", "1200", "05-12-2019-28-01-2020", "CAPI", "Kirghiz,Russian"],
"KOR": ["53", "South_Korea", "KOR", "EastAsia", "1245", "24-12-2017-16-01-2018", "CAPI", "Korean"],
"LBN": ["30", "Lebanon", "LBN", "Semetic", "1200", "04-06-2018-18-06-2018", "CAPI", "Arabic"],
"LBY": ["31", "Libya", "LBY", "Semetic", "1196", "12-12-2021-26-01-2022", "CAPI", "Arabic"],
"MAC": ["32", "Macau_SAR", "MAC", "EastAsia", "1023", "03-10-2019-17-12-2019", "CAPI", "Chinese"],
"MAR": ["37", "Morocco", "MAR", "Semetic", "1200", "01-11-2021-19-12-2021", "PAPI", "Arabic"],
"MDV": ["34", "Maldives", "MDV", "Indo-Iranian", "1038", "01-09-2021-01-10-2021", "CAPI", "Dhivehi"],
"MEX": ["35", "Mexico", "MEX", "Latin", "1739", "18-01-2018-02-05-2018", "PAPI", "Spanish"],
"MMR": ["38", "Myanmar", "MMR", "EastAsia", "1200", "17-01-2020-03-03-2020", "CAPI", "Burmese"],
"MNG": ["36", "Mongolia", "MNG", "Turkic", "1638", "04-09-2019-06-02-2021", "CAPI", "Mongolian"],
"MYS": ["33", "Malaysia", "MYS", "EastAsia", "1313", "05-04-2018-21-05-2018", "CAWI/CAPI", "Malay,Chinese"],
"NGA": ["42", "Nigeria", "NGA", "SubSaharanAfrica", "1237", "19-12-2017-26-01-2018", "CAPI", "Hausa,Igbo,Yoruba,English"],
"NIC": ["41", "Nicaragua", "NIC", "Latin", "1200", "30-11-2019-05-01-2020", "CAPI", "Spanish"],
"NIR": ["43", "Northern_Ireland", "NIR", "Anglosphere", "447", "01-03-2022-07-09-2022", "CAPI/CAWI/Post/Video_interviewing", "English"],
"NLD": ["39", "Netherlands", "NLD", "Germanic", "2145", "03-01-2022-25-01-2022", "CAWI", "Dutch"],
"NZL": ["40", "New_Zealand", "NZL", "Anglosphere", "1057", "04-07-2019-21-02-2020", "Mail/Post", "English"],
"PAK": ["44", "Pakistan", "PAK", "Indo-Iranian", "1995", "04-11-2018-11-12-2018", "CAPI", "Urdu"],
"PER": ["45", "Peru", "PER", "Latin", "1400", "17-08-2018-09-09-2018", "PAPI", "Spanish"],
"PHL": ["46", "Philippines", "PHL", "EastAsia", "1200", "03-12-2019-09-12-2019", "PAPI", "Bikol,Cebuano,Filipino,Ikolo,Tausug,Waray,Hiligaynon"],
"PRI": ["47", "Puerto_Rico", "PRI", "Latin", "1127", "16-03-2018-27-10-2018", "PAPI", "Spanish"],
"ROU": ["48", "Romania", "ROU", "Latin", "1257", "30-11-2017-02-04-2018", "CAPI", "Romanian"],
"RUS": ["49", "Russia", "RUS", "Slavic", "1810", "07-11-2017-29-12-2017", "CAPI/PAPI", "Russian"],
"SGP": ["51", "Singapore", "SGP", "EastAsia", "2012", "08-11-2019-15-03-2020", "PAPI", "English,Malay,Chinese"],
"SRB": ["50", "Serbia", "SRB", "Slavic", "1046", "20-05-2017-07-07-2017", "PAPI", "Serbian"],
"SVK": ["52", "Slovakia", "SVK", "Slavic", "1200", "19-01-2022-22-02-2022", "CAPI", "Slovak"],
"THA": ["56", "Thailand", "THA", "EastAsia", "1500", "01-12-2017-26-02-2018", "PAPI", "Thai"],
"TJK": ["55", "Tajikistan", "TJK", "Indo-Iranian", "1200", "08-01-2020-06-02-2020", "CAPI", "Tajik,Russian"],
"TUN": ["57", "Tunisia", "TUN", "Semetic", "1208", "26-04-2019-20-05-2019", "CAPI", "Arabic"],
"TUR": ["58", "Turkey", "TUR", "Turkic", "2415", "31-03-2018-21-05-2018", "PAPI", "Turkish"],
"TWN": ["54", "Taiwan_ROC", "TWN", "EastAsia", "1223", "25-03-2019-16-06-2019", "CAPI", "Chinese"],
"UKR": ["59", "Ukraine", "UKR", "Slavic", "1289", "25-07-2020-14-08-2020", "CAPI", "Ukrainian,Russian"],
"URY": ["61", "Uruguay", "URY", "Latin", "1000", "27-01-2022-22-03-2022", "CAPI", "Spanish"],
"USA": ["60", "United_States", "USA", "Anglosphere", "2596", "28-04-2017-31-05-2017", "CAWI/CATI", "English"],
"USN": ["67", "United_States_North", "USN", "Anglosphere", "2596", "28-04-2017-31-05-2017", "CAWI/CATI", "English"],
"USS": ["68", "United_States_South", "USS", "Anglosphere", "2596", "28-04-2017-31-05-2017", "CAWI/CATI", "English"],
"VEN": ["62", "Venezuela", "VEN", "Latin", "1190", "03-05-2021-26-07-2021", "PAPI", "Spanish"],
"VNM": ["63", "Vietnam", "VNM", "EastAsia", "1200", "15-12-2019-21-01-2020", "CAPI", "Vietnamese"],
"ZWE": ["64", "Zimbabwe", "ZWE", "SubSaharanAfrica", "1215", "11-02-2020-23-03-2020", "CAPI", "English,Shona,Ndebele"]
};



language_families = {
    'AND': 'Latin',
    'ARG': 'Latin',
    'AUS': 'Anglosphere',
    'BGD': 'Indo-Iranian',
    'ARM': 'Isolate',
    'BOL': 'Latin',
    'BRA': 'Latin',
    'MMR': 'EastAsia',
    'CAN': 'Anglosphere',
    'CHL': 'Latin',
    'CHN': 'EastAsia',
    'TWN': 'EastAsia',
    'COL': 'Latin',
    'CYP': 'Isolate',
    'CZE': 'Slavic',
    'ECU': 'Latin',
    'ETH': 'Semetic',
    'DEU': 'Germanic',
    'GRC': 'Isolate',
    'GTM': 'Latin',
    'HKG': 'EastAsia',
    'IDN': 'EastAsia',
    'IRN': 'Indo-Iranian',
    'IRQ': 'Semetic',
    'JPN': 'EastAsia',
    'KAZ': 'Turkic',
    'JOR': 'Semetic',
    'KEN': 'SubSaharanAfrica',
    'KOR': 'EastAsia',
    'KGZ': 'Turkic',
    'LBN': 'Semetic',
    'LBY': 'Semetic',
    'MAC': 'EastAsia',
    'MYS': 'EastAsia',
    'MDV': 'Indo-Iranian',
    'MEX': 'Latin',
    'MNG': 'Turkic',
    'MAR': 'Semetic',
    'NLD': 'Germanic',
    'NZL': 'Anglosphere',
    'NIC': 'Latin',
    'NGA': 'SubSaharanAfrica',
    'PAK': 'Indo-Iranian',
    'PER': 'Latin',
    'PHL': 'EastAsia',
    'PRI': 'Latin',
    'ROU': 'Latin',
    'RUS': 'Slavic',
    'SRB': 'Slavic',
    'SGP': 'EastAsia',
    'SVK': 'Slavic',
    'VNM': 'EastAsia',
    'ZWE': 'SubSaharanAfrica',
    'TJK': 'Indo-Iranian',
    'THA': 'EastAsia',
    'TUN': 'Semetic',
    'TUR': 'Turkic',
    'UKR': 'Slavic',
    'EGY': 'Semetic',
    'GBR': 'Anglosphere',
    'USA': 'Anglosphere',
    'URY': 'Latin',
    'VEN': 'Latin',
    'NIR': 'Anglosphere'
}

def test_vis():
    # RGB
    dict_langfam2color = {
        "Anglosphere": "(151, 0, 0)",  # dark red
        "EastAsia": "(0, 102, 102)",  # dark turquoise
        "Germanic": "(96, 96, 96)",  # grey
        "Indo-Iranian": "(153, 76, 0)",  # dark yellow
        "Isolate": "(153, 0, 76)",  # dark pink
        "Latin": "(153, 153, 0)",  # dark yellow
        "Semetic": "(0, 102, 0)",  # dark green
        "Slavic": "(0, 153, 153)",  # dark blue/green
        "SubSaharanAfrica": "(0, 0, 153)",  # dark blue
        "Turkic": "(76, 0, 153)"  # dark purple
    }
    dict_langfam2color = {k: tuple(map(lambda x: x / 255, literal_eval(v)))
            for k, v in dict_langfam2color.items()
    }
    # ----------------------------------------------------------------------

    language_counts = Counter(language_families.values())
    colors = [dict_langfam2color[fam] for fam in language_counts.keys()]

    plt.pie(language_counts.values(), labels=language_counts.keys(), autopct='%1.1f%%', colors=colors)
    plt.show();





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    test_vis()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
