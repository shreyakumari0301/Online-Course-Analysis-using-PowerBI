from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text data from Power BI
text = "Power BI Data Science Machine Learning AI Visualization"

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
