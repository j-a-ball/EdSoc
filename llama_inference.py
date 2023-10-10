from tqdm import tqdm
import subprocess
import os

def main():
    # 
    txt_dir = "jes-txts"
    data_dir = "data/7B_Q5_JES"
    #
    for dirpath, dirnames, filenames in os.walk(txt_dir):
        dirp = dirpath
        files = [file for file in filenames if file.endswith(".txt")]
    # Prompt
    p1 = """

### Example of how to code a Sociology of Education article on the basis of 12 selected categories, then store the results in JSON.
# JSON scheme: {"quantitative": bool, "qualitative": bool, "primary/secondary": bool, "tertiary": bool, "inequality": bool, "nonstructural": bool, "culture": bool, "school": bool, "state": bool, "labor": bool, "comparative": bool, "methods": bool}
example_article = '''The "Collective Mind" at
 Work: A Decade in the Life of
 U.S. Sociology of Education
 Sociology of Education
 86(4) 273-279
 © American Sociological Association 20 1 3
 DOI: 10.1177/0038040713503304
 http://soe.sagepub.com
 §SAGE
 Steven Brint

             METHOD
 Between 1999 and 2008, 168 articles appeared in
 Sociology of Education , between 3 and 5 articles
 in each of four issues during the year. (In 2000,
 the journal published a special extra issue, which
 included essays about current thinking about key
 issues in the subdiscipline.) I coded each of the
 articles that met my criteria for inclusion in four
 ways. First, I classified the articles by methodol-
 ogy: either quantitative or qualitative. In a few
 cases, both types of methodology were equally
 prominent. I noted these articles separately. Sec-
 ond, I classified the level of education addressed
 in the article: primary/secondary or tertiary. In
 some cases, articles concerned both primary/sec-
 ondary and tertiary education. In these cases, I
 did not classify the articles. Third, I classified
 the articles into one of eight major topical catego-
 ries: (1) inequality, (2) "nonstructural" sources of
 achievement, (3) culture/ideology, (4) school
 organization/school effects, (5) state/politics, (6)
 labor market/labor market transitions, (7) compar-
 ative/historical analysis, and (8) methods. Finally,
 I classified articles into a more fine-grained topi-
 cal scheme of 22 categories in all. I will concen-
 trate my discussion of content on the distribution
 of articles into the eight major topical categories
 listed above. Therefore, let me elaborate the con-
 ventions that I used in coding articles into these
 categories.
 I classified the articles on the basis of the pri-
 mary emphasis in the article. Where possible, I
 tried to classify under one category only. I classi-
 fied only a handful of articles under more than one
 category, because I could not determine their pri-
 mary emphasis. I made a distinction in coding
 between the major structural bases of inequality
 in American society (i.e., social class, race/ethnic-
 ity, immigration status, and gender) and social
 structures and behaviors that vary within these
 broad strata (such as family structure or student
 work effort). I reserved the category "nonstruc-
 tural sources of achievement" for articles that
 took up these latter sources of variation in educa-
 tional outcomes. Thus, articles about the effects of
 work effort, drinking behavior, or obesity on stu-
 dent achievement were coded into this category,
 but articles about the effects of wealth or immigra-
 tion status on educational attainment were coded
 into the "inequality and schools" category.
 In this coding scheme, "culture/ideology"
 includes articles both on cultural influences on
 the organization of schooling and the influences
 of the organization of schooling on culture. An
 example of the former would be an article on the
 interpersonal strategies used by high-achieving
 students to mask their school achievements in set-
 tings that belittle intellectuality. An example of
 the latter would be an article on the effects of edu-
 cational attainment on attitudes about public
 affairs.
 I will not make strong claims for the accuracy
 of my coding. In some cases, other equally expert
 coders would likely have made different coding
 choices. However, many of the articles were not
 difficult to code, and I believe the measurement
 error due to coding mistakes is relatively minor.'''
# The example article describes a method for qualitative coding, so "quantitative" is False and "qualitative" is True. "primary/secondary" and "tertiary" are both False, because the article does not focus on a specific level of education. "methods" is True, because the article is mainly a review of methods used in the field. "methods" is the article's primary designation, so all 7 remaining categories must be False.
example_json = {"quantitative": False, "qualitative": True, "primary/secondary": False, "tertiary": False, "inequality": False, "nonstructural": False, "culture": False, "school": False, "state": False, "labor": False, "comparative": False, "methods": True}
 
### Code a new article using the same method.  
new_article = '''"""
    # + Soc of Ed article +
    p2 = """''' 
# JSON scheme: {"quantitative": bool, "qualitative": bool, "primary/secondary": bool, "tertiary": bool, "inequality": bool, "nonstructural": bool, "culture": bool, "school": bool, "state": bool, "labor": bool, "comparative": bool, "methods": bool}
# Return only JSON with correct categorical codes inferred from `new_article`
new_json = """
# Generate responses for each article
    responses = []
    for file in tqdm(files):
        input = ""
        with open(os.path.join(dirp, file), "r") as infile:
            pgs = infile.read().split("<newpage>")
        input = "\n".join(pgs[:3])
        prompt = p1 + input + p2
        response = subprocess.run(["../codellama/llama.cpp/main", "-m", "../codellama/llama.cpp/models/7B/code-base-Q5_K.bin", "-c", "8000", "-n", "80", "--multiline_input", "-p", prompt], capture_output=True)
        response = response.stdout.decode("utf-8")
        # Save
        with open(os.path.join(data_dir, file), "w") as outfile:
            outfile.write(response)
        responses.append(response)
    with open(os.path.join(data_dir, "responses.txt"), "w") as outfile:
        outfile.write("<newpage>".join(responses))

if __name__ == "__main__":
    main()