import pandas as pd
import json

def load_annotated_data(filepath: str) -> pd.DataFrame:
    """تحميل البيانات المشروحة بصيغة JSON وتحويلها إلى DataFrame"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return pd.DataFrame(data)

def analyze_morpho_syntactic_distribution(df: pd.DataFrame):
    """
    تحليل التوزيع الصرفي-النحوي (الشكل 1 و 2 في البحث).
    """
    print("--- التوزيع النحوي (Grammatical Structure) ---")
    # حساب نسبة Verbal مقابل Nominal
    structure_counts = df['grammatical_structure'].value_counts(normalize=True) * 100
    print(structure_counts)
    print("\n")

    print("--- أشكال التشبيه (Simile Forms) ---")
    similes_df = df[df['figure_type'] == 'simile']
    simile_counts = similes_df['marker_explicitness'].value_counts(normalize=True) * 100
    print(simile_counts)
    print("\n")

def analyze_form_function_correlation(df: pd.DataFrame):
    """
    تحليل التقاطع بين البنية النحوية والمجال الدلالي والوظيفة البراغماتية.
    (القسم 4.1.4 Form-Function Correlations).
    """
    print("--- التقاطع بين (Source Domain) و (Pragmatic Function) ---")
    # Cross-tabulation باستخدام بانداز
    cross_tab = pd.crosstab(df['source_domain'], df['pragmatic_function'])
    print(cross_tab)
    print("\n")
    
    print("--- التقاطع بين التركيب النحوي (Structure) ومجال الهدف (Target Domain) ---")
    structure_target_ct = pd.crosstab(df['grammatical_structure'], df['target_domain'])
    print(structure_target_ct)
    print("\n")

if __name__ == "__main__":
    # بافتراض أن البيانات المشروحة موجودة في هذا المسار وتحتوي على الأعمدة:
    # ['verse', 'figure_type', 'grammatical_structure', 'source_domain', 'target_domain', 'pragmatic_function', 'marker_explicitness']
    
    # df = load_annotated_data('../../data/annotations/final_annotated_corpus.json')
    # analyze_morpho_syntactic_distribution(df)
    # analyze_form_function_correlation(df)
    pass
