
import re

def count_words(text):
    # Remove markdown headers and markers
    text = re.sub(r'#+\s+', '', text)
    text = re.sub(r'\*\*', '', text)
    # Simple word count
    words = text.split()
    return len(words)

# B1 Paragraphs from raw_content.md
p1 = "At over a million square meters, and with over 1,200 stores, the Dubai Mall is huge in mall terms. The 750,000 people who visit it every week can find almost any product that meets their demands. Such mega-malls could be seen as a natural home for Generation Y, the biggest-spending and most demanding generation of consumers the world has ever seen."
p2 = "Generation Y is the name given to the group of people born between the late 1970s and mid-1990s. Their lives have happened at the same time as huge financial changes in the way we spend our money, and members of this group are demonstrating more and more financial behaviors across a range of countries and cultures."
p3 = "While their parents' generation knew many store owners personally when they were growing up, members of Generation Y are more likely to buy from huge multinational companies like Walmart. The biggest group of stores on the planet shows no signs of stopping. They grew from 8,500 stores in 15 countries in 2011 to over 11,500 stores in 28 different countries in 2015. That year Walmart made sales of just under 500 billion U.S. dollars, which is bigger than the GDP of 165 countries."
p4 = "While consumers of the Generation Y period can choose from a huge range of products at giant shopping malls, they have even more choice online. In just over a decade, Internet shopping saw huge growth. In the U.K., for example, consumers spent £800 million online in 2000; by 2015 this had grown to £114 billion. Amazon, the world's largest online store, sells such a wide variety of products they have to be kept in huge buildings the size of ten soccer fields."
p5 = "Gen Y-ers are the main target for many companies because of their spending power and attitude to shopping. In the U.S. alone, as a group they have $170 billion to spend and 31% earn enough money to live the life they choose. Unfortunately for companies, they are considered the hardest group to sell to. A large portion of Generation Y claim they are not influenced by advertising. Instead, one in three read blogs to seek suggestions and reviews before deciding what to buy. The group does not like to be influenced and are unlikely to believe any advertising message, but they do expect companies to personally interact with them on social media."
p6 = "The older and richer Gen Y consumers become, the more important it is for companies to understand them. If a company can use technology to personalize its products and services, it might just gain some of the richest technology-loving customers in history."

paragraphs = [p1, p2, p3, p4, p5, p6]
total_b1 = 0
for i, p in enumerate(paragraphs, 1):
    count = count_words(p)
    print(f"P{i}: {count} words")
    total_b1 += count

print(f"Total B1 words: {total_b1}")
print(f"Target B2 words (+15%): {round(total_b1 * 1.15)}")
