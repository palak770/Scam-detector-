import pandas as pd
import re
from urllib.parse import urlparse
import nltk

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

# ---------------------------
# 1. Metadata Extraction
# ---------------------------


def extract_metadata(df):
    """
    Extract extra information from articles:
    - Domain from source URL
    - Content length
    - Number of hashtags
    more metadata here (e.g., mentions, emojis, special patterns)
    """
    
    df['domain'] = df['source'].apply(lambda x: urlparse(x).netloc if pd.notnull(x) else 'unknown')
    df['content_length'] = df['content'].apply(lambda x: len(str(x)))
    df['num_hashtags'] = df['content'].apply(lambda x: str(x).count('#'))
    df['num_mentions'] = df['content'].apply(lambda x: str(x).count('@'))
    df['num_urls'] = df['content'].apply(lambda x: len(re.findall(r'http[s]?://\S+', str(x))))
    df['num_emojis'] = df['content'].apply(lambda x: len(re.findall(r'[^\w\s,]', str(x))))
    df['num_special_chars'] = df['content'].apply(lambda x: len(re.findall(r'[^a-zA-Z0-9\s]', str(x))))
    df['num_words'] = df['content'].apply(lambda x: len(str(x).split()))
    df['num_unique_words'] = df['content'].apply(lambda x: len(set(str(x).split())))
    df['num_stopwords'] = df['content'].apply(lambda x: len([word for word in word_tokenize(str(x).lower()) if word in stop_words]))
    df['num_sentences'] = df['content'].apply(lambda x: len(nltk.sent_tokenize(str(x))))
    df['avg_word_length'] = df['content'].apply(lambda x: sum(len(word) for word in str(x).split()) / (len(str(x).split()) + 1e-5))
    df['avg_sentence_length'] = df['content'].apply(lambda x: sum(len(sentence.split()) for sentence in nltk.sent_tokenize(str(x))) / (len(nltk.sent_tokenize(str(x))) + 1e-5))
    return df
# ---------------------------
# 2. Data Cleaning
# ---------------------------

def clean_text(text):
    """
    Clean the text data:
    - Lowercase
    - Remove URLs, mentions, hashtags
    - Remove special characters and numbers
    - Remove extra spaces
    """
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#','', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def clean_dataframe(df):
    """
    Apply text cleaning to the 'content' column of the dataframe.
    """
    df['cleaned_content'] = df['content'].apply(clean_text)
    return df
# ---------------------------
# 3. Data Validation
# ---------------------------
def validate_data(df):
    """
    Validate the dataframe:
    - Check for missing values in critical columns
    - Ensure data types are correct
    """
    critical_columns = ['content', 'source']
    for col in critical_columns:
        if df[col].isnull().any():
            raise ValueError(f"Missing values found in critical column: {col}")
    if not pd.api.types.is_string_dtype(df['content']):
        raise TypeError("Column 'content' must be of type string")
    if not pd.api.types.is_string_dtype(df['source']):
        raise TypeError("Column 'source' must be of type string")
    return True
# Example usage:
if __name__ == "__main__":
    # Sample data
    data = {
        'content': ["Check out this link: https://example.com #exciting @user", 
                    "Another article without a link!"],
        'source': ["https://news.example.com/article1", "https://blog.example.com/post"]
    }
    df = pd.DataFrame(data) 
    # Validate data
    validate_data(df)
    # Clean data
    df = clean_dataframe(df)
    # Extract metadata
    df = extract_metadata(df)
    print(df)

# ---------------------------
# 3. Suspicious Score (Optional)
# ---------------------------
def suspicious_score(text):
    """
    Assign a small score to indicate potentially fake or suspicious content.
    You can create your own scoring rules here:
    - Count keywords (fake, hoax, rumor)
    - Detect clickbait patterns
    - Add weighting for suspicious phrases
    """
    score = 0
    keywords = ["fake", "hoax", "rumor", "breaking", "shocking"]
    for word in keywords:
        score += text.lower().count(word)
    if re.search(r'click here|you won|free gift', text, re.IGNORECASE):
        score += 2
    return score
def add_suspicious_score(df):
    """
    Apply suspicious score calculation to the 'content' column of the dataframe.
    """
    df['suspicious_score'] = df['content'].apply(suspicious_score)
    return df
# Example usage:
if __name__ == "__main__":
    # Sample data
    data = {
        'content': ["This is a fake news article! Click here to find out more.",
                    "This is a legitimate news article."],
        'source': ["https://news.example.com/article1", "https://blog.example.com/post"]
    }
    df = pd.DataFrame(data)
    # Validate data
    validate_data(df)
    # Clean data
    df = clean_dataframe(df)
    # Extract metadata
    df = extract_metadata(df)
    # Add suspicious score
    df = add_suspicious_score(df)
    print(df)


# ---------------------------
# 4. Data Agent Class
# ---------------------------

class DataAgent:
     def __init__(self, path):
         
    def __init__(self, dataframe):
        self.df = dataframe
        validate_data(self.df)
        self.df = clean_dataframe(self.df)
        self.df = extract_metadata(self.df)
        self.df = add_suspicious_score(self.df)
    def get_dataframe(self):
        return self.df
    def save_to_csv(self, filepath):
        self.df.to_csv(filepath, index=False)
        return f"Data saved to {filepath}"
    
    
