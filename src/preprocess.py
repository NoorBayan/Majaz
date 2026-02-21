import re
import json

def normalize_arabic_text(text: str) -> str:
    """
    يقوم بمعالجة النص القرآني المسبقة بناءً على المنهجية:
    - الاحتفاظ بالتشكيل (Tashkīl) بالكامل لأغراض التحليل النحوي والإيقاعي.
    - توحيد أشكال الألف لتسهيل البحث عن الجذور.
    - إزالة الرموز غير النصية (Unicode artifacts).
    """
    # 1. توحيد أشكال الألف (Alef Normalization)
    text = re.sub(r'[إأآا]', 'ا', text)
    
    # 2. إزالة علامات الوقف أو الرموز الخاصة التي قد تعيق البحث البرمجي (اختياري حسب الحاجة)
    # الاحتفاظ بالحروف العربية والتشكيل والمسافات فقط
    text = re.sub(r'[^\u0600-\u06FF\s]', '', text)
    
    # 3. إزالة المسافات الزائدة
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def process_corpus(input_filepath: str, output_filepath: str):
    """
    قراءة ملف البيانات الخام (مثال: Tanzil XML أو JSON) ومعالجته وحفظه.
    """
    with open(input_filepath, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
        
    processed_data = []
    for verse in raw_data:
        processed_verse = {
            "verse_key": verse.get("verse_key"), # مثال: "2:7"
            "original_text": verse.get("text"),
            "processed_text": normalize_arabic_text(verse.get("text"))
        }
        processed_data.append(processed_verse)
        
    with open(output_filepath, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=4)
        
    print(f"تمت المعالجة بنجاح. عدد الآيات: {len(processed_data)}")

if __name__ == "__main__":
    # مثال للاستخدام
    # process_corpus('../../data/raw/tanzil_quran.json', '../../data/processed/cleaned_quran.json')
    pass
