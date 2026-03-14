"""
domain_router.py
----------------
Routing library for the Clinical Trial Intelligence Platform (CTIP).

Provides three public functions:
    create_routing_table()  — builds the routing table dict and writes it to JSON
    load_routing_table()    — loads the JSON and returns it as a dict
    resolve_domain()        — looks up a disease search term and returns routing metadata

Usage in trial_getter.ipynb (or any other notebook):
    from domain_router import create_routing_table, load_routing_table, resolve_domain

    create_routing_table()          # run once at setup, or any time the table is edited
    routing_table = load_routing_table()
    result = resolve_domain("myeloma", routing_table)

JSON output: domain_routing_table.json (same directory as this file)

To add a new disease:
    1. Add an entry to ROUTING_TABLE below
    2. Call create_routing_table() to regenerate the JSON
    3. The updated table will be picked up automatically on next load_routing_table() call
"""

import json
import os

# --- Path Configuration ---
_DIR = os.path.dirname(os.path.abspath(__file__))
ROUTING_TABLE_PATH = os.path.join(_DIR, "domain_routing_table.json")

# --- Routing Table ---
# Each entry maps a lowercase disease search term to:
#   domain      : broad disease category
#   subdomain   : specific disease class within domain
#   conference  : primary conference source for mechanism-rich abstracts
#
# Conference abbreviations:
#   ASH         American Society of Hematology
#   MDS_Congress Movement Disorder Society Congress (NOT myelodysplastic syndrome)
#   CTAD        Clinical Trials on Alzheimer's Disease
#   ECTRIMS     European Committee for Treatment and Research in Multiple Sclerosis
#   AES         American Epilepsy Society
#   AAN         American Academy of Neurology
#   CROI        Conference on Retroviruses and Opportunistic Infections
#   EASL        European Association for the Study of the Liver
#   UNION       International Union Against Tuberculosis and Lung Disease
#   ECCMID      European Congress of Clinical Microbiology and Infectious Diseases
#   OPTIONS     Options for the Control of Influenza
#   IASLC       International Association for the Study of Lung Cancer
#   SABCS       San Antonio Breast Cancer Symposium
#   ASCO        American Society of Clinical Oncology
#   EULAR       European Alliance of Associations for Rheumatology
#   AAD         American Academy of Dermatology
#   UEGW        United European Gastroenterology Week
#   ESC         European Society of Cardiology
#   ADA         American Diabetes Association
#   ObesityWeek Obesity Society Annual Meeting
#   PubMed_only No dominant conference — PubMed enrichment only

ROUTING_TABLE = {

    # -------------------------------------------------------------------------
    # Hematology
    # -------------------------------------------------------------------------
    "myeloma":                          {"domain": "hematology", "subdomain": "plasma_cell",        "conference": "ASH"},
    "multiple myeloma":                 {"domain": "hematology", "subdomain": "plasma_cell",        "conference": "ASH"},
    "smoldering myeloma":               {"domain": "hematology", "subdomain": "plasma_cell",        "conference": "ASH"},
    "leukemia":                         {"domain": "hematology", "subdomain": "leukemia",           "conference": "ASH"},
    "aml":                              {"domain": "hematology", "subdomain": "leukemia",           "conference": "ASH"},
    "acute myeloid leukemia":           {"domain": "hematology", "subdomain": "leukemia",           "conference": "ASH"},
    "cll":                              {"domain": "hematology", "subdomain": "leukemia",           "conference": "ASH"},
    "chronic lymphocytic leukemia":     {"domain": "hematology", "subdomain": "leukemia",           "conference": "ASH"},
    "all":                              {"domain": "hematology", "subdomain": "leukemia",           "conference": "ASH"},
    "acute lymphoblastic leukemia":     {"domain": "hematology", "subdomain": "leukemia",           "conference": "ASH"},
    "cml":                              {"domain": "hematology", "subdomain": "leukemia",           "conference": "ASH"},
    "chronic myeloid leukemia":         {"domain": "hematology", "subdomain": "leukemia",           "conference": "ASH"},
    "lymphoma":                         {"domain": "hematology", "subdomain": "lymphoma",           "conference": "ASH"},
    "dlbcl":                            {"domain": "hematology", "subdomain": "lymphoma",           "conference": "ASH"},
    "diffuse large b-cell lymphoma":    {"domain": "hematology", "subdomain": "lymphoma",           "conference": "ASH"},
    "follicular lymphoma":              {"domain": "hematology", "subdomain": "lymphoma",           "conference": "ASH"},
    "hodgkin lymphoma":                 {"domain": "hematology", "subdomain": "lymphoma",           "conference": "ASH"},
    "myelodysplastic syndrome":         {"domain": "hematology", "subdomain": "myelodysplastic",    "conference": "ASH"},
    "myelodysplastic":                  {"domain": "hematology", "subdomain": "myelodysplastic",    "conference": "ASH"},
    "myelofibrosis":                    {"domain": "hematology", "subdomain": "myeloproliferative", "conference": "ASH"},
    "sickle cell":                      {"domain": "hematology", "subdomain": "hemoglobinopathy",   "conference": "ASH"},
    "sickle cell disease":              {"domain": "hematology", "subdomain": "hemoglobinopathy",   "conference": "ASH"},
    "thalassemia":                      {"domain": "hematology", "subdomain": "hemoglobinopathy",   "conference": "ASH"},

    # -------------------------------------------------------------------------
    # Neurology: Parkinson's / MSA / PSP
    # -------------------------------------------------------------------------
    "parkinson":                        {"domain": "neurology", "subdomain": "parkinsonian",    "conference": "MDS_Congress"},
    "parkinson's":                      {"domain": "neurology", "subdomain": "parkinsonian",    "conference": "MDS_Congress"},
    "parkinson's disease":              {"domain": "neurology", "subdomain": "parkinsonian",    "conference": "MDS_Congress"},
    "pd":                               {"domain": "neurology", "subdomain": "parkinsonian",    "conference": "MDS_Congress"},
    "msa":                              {"domain": "neurology", "subdomain": "parkinsonian",    "conference": "MDS_Congress"},
    "multiple system atrophy":          {"domain": "neurology", "subdomain": "parkinsonian",    "conference": "MDS_Congress"},
    "psp":                              {"domain": "neurology", "subdomain": "parkinsonian",    "conference": "MDS_Congress"},
    "progressive supranuclear palsy":   {"domain": "neurology", "subdomain": "parkinsonian",    "conference": "MDS_Congress"},
    "corticobasal syndrome":            {"domain": "neurology", "subdomain": "parkinsonian",    "conference": "MDS_Congress"},
    "parkinsons":                   {"domain": "neurology", "subdomain": "parkinsonian", "conference": "MDS_Congress"},
    "parkinson disease":            {"domain": "neurology", "subdomain": "parkinsonian", "conference": "MDS_Congress"},
    "pdisease":                     {"domain": "neurology", "subdomain": "parkinsonian", "conference": "MDS_Congress"},

    # -------------------------------------------------------------------------
    # Neurology: Alzheimer's / Dementia
    # -------------------------------------------------------------------------
    "alzheimer":                        {"domain": "neurology", "subdomain": "dementia",        "conference": "CTAD"},
    "alzheimer's":                      {"domain": "neurology", "subdomain": "dementia",        "conference": "CTAD"},
    "alzheimer's disease":              {"domain": "neurology", "subdomain": "dementia",        "conference": "CTAD"},
    "ad":                               {"domain": "neurology", "subdomain": "dementia",        "conference": "CTAD"},
    "dementia":                         {"domain": "neurology", "subdomain": "dementia",        "conference": "CTAD"},
    "lewy body dementia":               {"domain": "neurology", "subdomain": "dementia",        "conference": "CTAD"},

    # -------------------------------------------------------------------------
    # Neurology: Multiple Sclerosis
    # -------------------------------------------------------------------------
    "multiple sclerosis":               {"domain": "neurology", "subdomain": "demyelinating",   "conference": "ECTRIMS"},
    "ms":                               {"domain": "neurology", "subdomain": "demyelinating",   "conference": "ECTRIMS"},
    "relapsing ms":                     {"domain": "neurology", "subdomain": "demyelinating",   "conference": "ECTRIMS"},
    "rrms":                             {"domain": "neurology", "subdomain": "demyelinating",   "conference": "ECTRIMS"},
    "ppms":                             {"domain": "neurology", "subdomain": "demyelinating",   "conference": "ECTRIMS"},
    "spms":                             {"domain": "neurology", "subdomain": "demyelinating",   "conference": "ECTRIMS"},
    "neuromyelitis optica":             {"domain": "neurology", "subdomain": "demyelinating",   "conference": "ECTRIMS"},
    "nmosd":                            {"domain": "neurology", "subdomain": "demyelinating",   "conference": "ECTRIMS"},

    # -------------------------------------------------------------------------
    # Neurology: Epilepsy
    # -------------------------------------------------------------------------
    "epilepsy":                         {"domain": "neurology", "subdomain": "epilepsy",        "conference": "AES"},
    "seizure":                          {"domain": "neurology", "subdomain": "epilepsy",        "conference": "AES"},
    "dravet syndrome":                  {"domain": "neurology", "subdomain": "epilepsy",        "conference": "AES"},
    "lennox-gastaut":                   {"domain": "neurology", "subdomain": "epilepsy",        "conference": "AES"},

    # -------------------------------------------------------------------------
    # Neurology: Motor Neuron / General CNS
    # -------------------------------------------------------------------------
    "als":                              {"domain": "neurology", "subdomain": "motor_neuron",    "conference": "AAN"},
    "amyotrophic lateral sclerosis":    {"domain": "neurology", "subdomain": "motor_neuron",    "conference": "AAN"},
    "huntington":                       {"domain": "neurology", "subdomain": "neurodegeneration","conference": "AAN"},
    "huntington's disease":             {"domain": "neurology", "subdomain": "neurodegeneration","conference": "AAN"},
    "spinal muscular atrophy":          {"domain": "neurology", "subdomain": "motor_neuron",    "conference": "AAN"},
    "sma":                              {"domain": "neurology", "subdomain": "motor_neuron",    "conference": "AAN"},

    # -------------------------------------------------------------------------
    # Infectious Disease
    # -------------------------------------------------------------------------
    "hiv":                              {"domain": "infectious_disease", "subdomain": "retroviral",         "conference": "CROI"},
    "hiv/aids":                         {"domain": "infectious_disease", "subdomain": "retroviral",         "conference": "CROI"},
    "aids":                             {"domain": "infectious_disease", "subdomain": "retroviral",         "conference": "CROI"},
    "hepatitis b":                      {"domain": "infectious_disease", "subdomain": "viral_hepatitis",    "conference": "EASL"},
    "hepatitis c":                      {"domain": "infectious_disease", "subdomain": "viral_hepatitis",    "conference": "EASL"},
    "hbv":                              {"domain": "infectious_disease", "subdomain": "viral_hepatitis",    "conference": "EASL"},
    "hcv":                              {"domain": "infectious_disease", "subdomain": "viral_hepatitis",    "conference": "EASL"},
    "tuberculosis":                     {"domain": "infectious_disease", "subdomain": "bacterial",          "conference": "UNION"},
    "tb":                               {"domain": "infectious_disease", "subdomain": "bacterial",          "conference": "UNION"},
    "covid":                            {"domain": "infectious_disease", "subdomain": "coronavirus",        "conference": "ECCMID"},
    "covid-19":                         {"domain": "infectious_disease", "subdomain": "coronavirus",        "conference": "ECCMID"},
    "sars-cov-2":                       {"domain": "infectious_disease", "subdomain": "coronavirus",        "conference": "ECCMID"},
    "influenza":                        {"domain": "infectious_disease", "subdomain": "respiratory_viral",  "conference": "OPTIONS"},
    "fungal infection":                 {"domain": "infectious_disease", "subdomain": "fungal",             "conference": "ECCMID"},
    "aspergillosis":                    {"domain": "infectious_disease", "subdomain": "fungal",             "conference": "ECCMID"},


    # -------------------------------------------------------------------------
    # Infectious Disease: HIV
    # -------------------------------------------------------------------------
    # CROI = Conference on Retroviruses and Opportunistic Infections
    # Primary conference for HIV/AIDS therapeutic and prevention research
    # -------------------------------------------------------------------------
    "hiv":                              {"domain": "infectious_disease", "subdomain": "hiv", "conference": "CROI"},
    "hiv-1":                            {"domain": "infectious_disease", "subdomain": "hiv", "conference": "CROI"},
    "hiv-2":                            {"domain": "infectious_disease", "subdomain": "hiv", "conference": "CROI"},
    "human immunodeficiency virus":     {"domain": "infectious_disease", "subdomain": "hiv", "conference": "CROI"},
    "aids":                             {"domain": "infectious_disease", "subdomain": "hiv", "conference": "CROI"},
    "acquired immunodeficiency syndrome": {"domain": "infectious_disease", "subdomain": "hiv", "conference": "CROI"},
   
    # -------------------------------------------------------------------------
    # Oncology (solid tumors)
    # -------------------------------------------------------------------------
    "lung cancer":                      {"domain": "oncology", "subdomain": "thoracic",          "conference": "IASLC"},
    "nsclc":                            {"domain": "oncology", "subdomain": "thoracic",          "conference": "IASLC"},
    "sclc":                             {"domain": "oncology", "subdomain": "thoracic",          "conference": "IASLC"},
    "breast cancer":                    {"domain": "oncology", "subdomain": "breast",            "conference": "SABCS"},
    "her2 breast cancer":               {"domain": "oncology", "subdomain": "breast",            "conference": "SABCS"},
    "triple negative breast cancer":    {"domain": "oncology", "subdomain": "breast",            "conference": "SABCS"},
    "tnbc":                             {"domain": "oncology", "subdomain": "breast",            "conference": "SABCS"},
    "colorectal cancer":                {"domain": "oncology", "subdomain": "gastrointestinal",  "conference": "ASCO"},
    "crc":                              {"domain": "oncology", "subdomain": "gastrointestinal",  "conference": "ASCO"},
    "prostate cancer":                  {"domain": "oncology", "subdomain": "genitourinary",     "conference": "ASCO"},
    "melanoma":                         {"domain": "oncology", "subdomain": "skin",              "conference": "ASCO"},
    "pancreatic cancer":                {"domain": "oncology", "subdomain": "gastrointestinal",  "conference": "ASCO"},
    "renal cell carcinoma":             {"domain": "oncology", "subdomain": "genitourinary",     "conference": "ASCO"},
    "rcc":                              {"domain": "oncology", "subdomain": "genitourinary",     "conference": "ASCO"},
    "hepatocellular carcinoma":         {"domain": "oncology", "subdomain": "gastrointestinal",  "conference": "ASCO"},
    "hcc":                              {"domain": "oncology", "subdomain": "gastrointestinal",  "conference": "ASCO"},
    "ovarian cancer":                   {"domain": "oncology", "subdomain": "gynecologic",       "conference": "ASCO"},
    "glioblastoma":                     {"domain": "oncology", "subdomain": "cns_tumor",         "conference": "ASCO"},
    "gbm":                              {"domain": "oncology", "subdomain": "cns_tumor",         "conference": "ASCO"},

    # -------------------------------------------------------------------------
    # Immunology / Rheumatology
    # -------------------------------------------------------------------------
    "rheumatoid arthritis":             {"domain": "immunology", "subdomain": "autoimmune_joint",    "conference": "EULAR"},
    "ra":                               {"domain": "immunology", "subdomain": "autoimmune_joint",    "conference": "EULAR"},
    "lupus":                            {"domain": "immunology", "subdomain": "autoimmune_systemic", "conference": "EULAR"},
    "sle":                              {"domain": "immunology", "subdomain": "autoimmune_systemic", "conference": "EULAR"},
    "systemic lupus erythematosus":     {"domain": "immunology", "subdomain": "autoimmune_systemic", "conference": "EULAR"},
    "psoriasis":                        {"domain": "immunology", "subdomain": "autoimmune_skin",     "conference": "AAD"},
    "psoriatic arthritis":              {"domain": "immunology", "subdomain": "autoimmune_joint",    "conference": "EULAR"},
    "ankylosing spondylitis":           {"domain": "immunology", "subdomain": "autoimmune_joint",    "conference": "EULAR"},
    "crohn":                            {"domain": "immunology", "subdomain": "ibd",                 "conference": "UEGW"},
    "crohn's disease":                  {"domain": "immunology", "subdomain": "ibd",                 "conference": "UEGW"},
    "ulcerative colitis":               {"domain": "immunology", "subdomain": "ibd",                 "conference": "UEGW"},
    "ibd":                              {"domain": "immunology", "subdomain": "ibd",                 "conference": "UEGW"},

    # -------------------------------------------------------------------------
    # Cardiovascular
    # -------------------------------------------------------------------------
    "heart failure":                    {"domain": "cardiovascular", "subdomain": "heart_failure",  "conference": "ESC"},
    "hfref":                            {"domain": "cardiovascular", "subdomain": "heart_failure",  "conference": "ESC"},
    "hfpef":                            {"domain": "cardiovascular", "subdomain": "heart_failure",  "conference": "ESC"},
    "atrial fibrillation":              {"domain": "cardiovascular", "subdomain": "arrhythmia",     "conference": "ESC"},
    "afib":                             {"domain": "cardiovascular", "subdomain": "arrhythmia",     "conference": "ESC"},
    "hypertension":                     {"domain": "cardiovascular", "subdomain": "hypertension",   "conference": "ESC"},
    "coronary artery disease":          {"domain": "cardiovascular", "subdomain": "coronary",       "conference": "ESC"},
    "cad":                              {"domain": "cardiovascular", "subdomain": "coronary",       "conference": "ESC"},

    # -------------------------------------------------------------------------
    # Metabolic
    # -------------------------------------------------------------------------
    "diabetes":                         {"domain": "metabolic", "subdomain": "type2_diabetes",  "conference": "ADA"},
    "type 2 diabetes":                  {"domain": "metabolic", "subdomain": "type2_diabetes",  "conference": "ADA"},
    "type 1 diabetes":                  {"domain": "metabolic", "subdomain": "type1_diabetes",  "conference": "ADA"},
    "t2d":                              {"domain": "metabolic", "subdomain": "type2_diabetes",  "conference": "ADA"},
    "t1d":                              {"domain": "metabolic", "subdomain": "type1_diabetes",  "conference": "ADA"},
    "obesity":                          {"domain": "metabolic", "subdomain": "obesity",         "conference": "ObesityWeek"},
    "nash":                             {"domain": "metabolic", "subdomain": "fatty_liver",     "conference": "EASL"},
    "nafld":                            {"domain": "metabolic", "subdomain": "fatty_liver",     "conference": "EASL"},
    "mash":                             {"domain": "metabolic", "subdomain": "fatty_liver",     "conference": "EASL"},
}

# --- Default fallback for unrecognized terms ---
_DEFAULT_ROUTE = {
    "domain":     "general",
    "subdomain":  "unclassified",
    "conference": "PubMed_only"
}


# =============================================================================
# Public API
# =============================================================================

def create_routing_table(path: str = ROUTING_TABLE_PATH) -> None:
    """
    Serialize ROUTING_TABLE to JSON and write to disk.
    Silently overwrites any existing file — call this any time the table is edited.

    Args:
        path: output path for the JSON file (defaults to same directory as this module)
    """
    with open(path, "w") as f:
        json.dump(ROUTING_TABLE, f, indent=2)
    print(f"✅ Routing table written: {path}  ({len(ROUTING_TABLE)} entries)")


def load_routing_table(path: str = ROUTING_TABLE_PATH) -> dict:
    """
    Load the routing table JSON from disk and return as a dict.
    Raises FileNotFoundError with a helpful message if the JSON doesn't exist yet.

    Args:
        path: path to the JSON file (defaults to same directory as this module)

    Returns:
        dict mapping disease search terms to routing metadata
    """
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Routing table not found at '{path}'.\n"
            f"Run create_routing_table() once to generate it."
        )
    with open(path, "r") as f:
        table = json.load(f)
    print(f"✅ Routing table loaded: {len(table)} entries from {path}")
    return table


def resolve_domain(search_term: str, routing_table: dict = None) -> dict:
    """
    Resolve a disease search term to domain, subdomain, and conference source.

    Looks up the normalized search term in the provided routing table (or falls
    back to the module-level ROUTING_TABLE if none is passed). Returns a dict
    matching the CTIP/TMTB routing contract.

    Args:
        search_term:   raw disease string (e.g. 'myeloma', 'HIV', 'MS')
        routing_table: dict from load_routing_table(); uses module ROUTING_TABLE if None

    Returns:
        {
            "search_term": str,
            "domain":      str,
            "subdomain":   str,
            "conference":  str
        }
    """
    table = routing_table if routing_table is not None else ROUTING_TABLE
    term  = search_term.lower().strip()
    route = table.get(term, None)

    if route is None:
        print(f"⚠️  '{term}' not found in routing table — falling back to PubMed only")
        print(f"    To add routing: insert an entry in ROUTING_TABLE in domain_router.py")
        print(f"    then call create_routing_table() to regenerate the JSON")
        route = _DEFAULT_ROUTE

    result = {
        "search_term": term,
        "domain":      route["domain"],
        "subdomain":   route["subdomain"],
        "conference":  route["conference"],
    }

    print(f"  Search term : '{term}'")
    print(f"  Domain      : {result['domain']}")
    print(f"  Subdomain   : {result['subdomain']}")
    print(f"  Conference  : {result['conference']}")

    return result
