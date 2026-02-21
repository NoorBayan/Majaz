import re
import json

# بناء التعابير النمطية (Regex) مع مراعاة وجود التشكيل (Diacritics)
# \p{M} أو [\u064B-\u065F] يمثل التشكيل في اليونيكود
DIACRITICS = r'[\u064B-\u065F]*'

SIMILE_PATTERNS = {
    "ka": re.compile(r'\bك' + DIACRITICS + r'[ا-ي]'), # حرف الكاف المتصل بكلمة (مثل: كَالنُّور)
    "mithl": re.compile(r'\bم' + DIACRITICS + r'ث' + DIACRITICS + r'ل\b'), # كلمة "مثل"
    "ka_anna": re.compile(r'\bك' + DIACRITICS + r'أ' + DIACRITICS + r'ن\b') # كلمة "كأن"
}

def extract_similes(processed_corpus_path: str, output_path: str):
    """
    يبحث في السجل عن الآيات التي تحتوي على أدوات التشبيه.
    (أشار البحث إلى العثور على 487 مرشحاً وتصفيتها لاحقاً إلى 402).
    """
    with open(processed_corpus_path, 'r', encoding='utf-8') as f:
        corpus = json.load(f)

    candidates = []
    
    for verse in corpus:
        text = verse['original_text'] # نستخدم النص الأصلي أو المعالج حسب الحاجة
        matched_particles = []
        
        for particle_name, pattern in SIMILE_PATTERNS.items():
            if pattern.search(text):
                matched_particles.append(particle_name)
                
        if matched_particles:
            verse['matched_particles'] = matched_particles
            candidates.append(verse)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(candidates, f, ensure_ascii=False, indent=4)
        
    print(f"تم استخراج {len(candidates)} آية مرشحة تحتوي على أدوات تشبيه.")

if __name__ == "__main__":
    # extract_similes('../../data/processed/cleaned_quran.json', '../../data/annotations/simile_candidates.json')
    pass
