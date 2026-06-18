import json
from pathlib import Path

def main():
    examples = []
    
    # 1. Pop culture
    examples.append({
        "qid": "q1",
        "difficulty": "easy",
        "question": "What is the capital of the country where the Eiffel Tower is located?",
        "gold_answer": "Paris",
        "context": [
            {"title": "Eiffel Tower", "text": "The Eiffel Tower is a landmark located in France."},
            {"title": "France", "text": "France is a country in Europe. The capital of France is Paris."}
        ]
    })
    
    examples.append({
        "qid": "q2",
        "difficulty": "medium",
        "question": "Which country was the composer of the Moonlight Sonata born in?",
        "gold_answer": "Germany",
        "context": [
            {"title": "Moonlight Sonata", "text": "The Moonlight Sonata was composed by Ludwig van Beethoven."},
            {"title": "Ludwig van Beethoven", "text": "Ludwig van Beethoven was a German composer born in Germany."}
        ]
    })
    
    examples.append({
        "qid": "q3",
        "difficulty": "easy",
        "question": "Who directed the movie that stars the actor who plays Iron Man?",
        "gold_answer": "Jon Favreau",
        "context": [
            {"title": "Iron Man", "text": "Iron Man is a 2008 film starring Robert Downey Jr. and directed by Jon Favreau."},
            {"title": "Robert Downey Jr.", "text": "Robert Downey Jr. is an actor who played the character Iron Man."}
        ]
    })
    
    # Let's generate the remaining 47 questions programmatically using a loop to ensure we have exactly 50 examples
    subjects = [
        ("Italy", "Rome", "Colosseum", "The Colosseum is a historical amphitheater located in Italy."),
        ("Japan", "Tokyo", "Mount Fuji", "Mount Fuji is the tallest mountain in Japan."),
        ("Egypt", "Cairo", "Great Pyramid of Giza", "The Great Pyramid of Giza is located in Egypt."),
        ("United Kingdom", "London", "Big Ben", "Big Ben is the nickname for the Great Bell of the clock in London, United Kingdom."),
        ("India", "New Delhi", "Taj Mahal", "The Taj Mahal is an ivory-white marble mausoleum in India."),
        ("China", "Beijing", "Great Wall of China", "The Great Wall of China is a historic fortification in China."),
        ("United States", "Washington D.C.", "Statue of Liberty", "The Statue of Liberty is a colossal neoclassical sculpture in the United States."),
        ("Australia", "Canberra", "Sydney Opera House", "The Sydney Opera House is located in Australia."),
        ("Brazil", "Brasilia", "Christ the Redeemer", "Christ the Redeemer is an Art Deco statue of Jesus Christ in Brazil."),
        ("Russia", "Moscow", "Kremlin", "The Kremlin is a fortified complex in the heart of Moscow, Russia."),
        ("Canada", "Ottawa", "CN Tower", "CN Tower is a signature icon of Toronto, Canada."),
        ("Spain", "Madrid", "Sagrada Familia", "Sagrada Familia is a large unfinished Roman Catholic minor basilica in Spain."),
        ("Greece", "Athens", "Parthenon", "The Parthenon is a former temple on the Athenian Acropolis, Greece."),
        ("Mexico", "Mexico City", "Chichen Itza", "Chichen Itza was a large pre-Columbian city built by the Maya people in Mexico."),
        ("Peru", "Lima", "Machu Picchu", "Machu Picchu is a 15th-century Inca citadel located in Peru."),
        ("Jordan", "Amman", "Petra", "Petra is a famous archaeological site in Jordan."),
        ("Cambodia", "Phnom Penh", "Angkor Wat", "Angkor Wat is a temple complex in Cambodia."),
        ("Turkey", "Ankara", "Hagia Sophia", "Hagia Sophia is a historic house of worship in Turkey."),
        ("United Arab Emirates", "Abu Dhabi", "Burj Khalifa", "Burj Khalifa is a skyscraper in Dubai, United Arab Emirates."),
        ("South Africa", "Pretoria", "Table Mountain", "Table Mountain is a flat-topped mountain forming a prominent landmark overlooking South Africa."),
    ]
    
    for i, (country, capital, landmark, desc) in enumerate(subjects):
        idx = 4 + i
        difficulty = "easy" if idx % 3 == 0 else ("medium" if idx % 3 == 1 else "hard")
        examples.append({
            "qid": f"q{idx}",
            "difficulty": difficulty,
            "question": f"What is the capital of the country where the {landmark} is located?",
            "gold_answer": capital,
            "context": [
                {"title": landmark, "text": desc},
                {"title": country, "text": f"{country} is a nation whose capital city is {capital}."}
            ]
        })
        
    # Let's add more subjects to make sure we reach 50 examples
    science_subjects = [
        ("Albert Einstein", "Germany", "Theory of Relativity", "The Theory of Relativity was developed by Albert Einstein."),
        ("Isaac Newton", "England", "Principia Mathematica", "Principia Mathematica is a work by Isaac Newton containing the laws of motion."),
        ("Marie Curie", "Poland", "discovery of Polonium", "Polonium was discovered by Marie Curie in 1898."),
        ("Charles Darwin", "England", "On the Origin of Species", "On the Origin of Species is a work of scientific literature by Charles Darwin."),
        ("Galileo Galilei", "Italy", "discovery of Jupiter moons", "The Galilean moons of Jupiter were discovered by Galileo Galilei."),
        ("Nikola Tesla", "Croatia", "alternating current system", "The alternating current system was patented by Nikola Tesla."),
        ("Louis Pasteur", "France", "pasteurization process", "Pasteurization is a process invented by Louis Pasteur."),
        ("Alexander Fleming", "Scotland", "discovery of penicillin", "Penicillin was discovered by Alexander Fleming in 1928."),
        ("Gregor Mendel", "Austria", "laws of Mendelian inheritance", "Mendelian inheritance was formulated by Gregor Mendel."),
        ("Dmitri Mendeleev", "Russia", "Periodic Table", "The Periodic Table of elements was created by Dmitri Mendeleev."),
        ("Ada Lovelace", "England", "first computer algorithm", "The first computer algorithm was written by Ada Lovelace."),
        ("Alan Turing", "England", "Turing Machine concept", "The Turing Machine concept was proposed by Alan Turing."),
        ("Stephen Hawking", "England", "Hawking radiation prediction", "Hawking radiation is black-body radiation predicted by Stephen Hawking."),
        ("Johannes Kepler", "Germany", "laws of planetary motion", "The laws of planetary motion were formulated by Johannes Kepler."),
        ("Thomas Edison", "United States", "invention of incandescent light bulb", "The incandescent light bulb was commercialized by Thomas Edison."),
        ("Michael Faraday", "England", "laws of electromagnetic induction", "Electromagnetic induction was discovered by Michael Faraday."),
        ("James Clerk Maxwell", "Scotland", "equations of electromagnetism", "Electromagnetic equations were formulated by James Clerk Maxwell."),
        ("Antoine Lavoisier", "France", "discovery of Oxygen role", "The role of oxygen in combustion was discovered by Antoine Lavoisier."),
        ("Robert Hooke", "England", "discovery of plant cells", "Plant cells were first discovered and named by Robert Hooke."),
        ("Richard Feynman", "United States", "Feynman diagrams development", "Feynman diagrams were developed by Richard Feynman."),
        ("Niels Bohr", "Denmark", "Bohr model of the atom", "The Bohr model of the atom was proposed by Niels Bohr."),
        ("Max Planck", "Germany", "quantum theory founding", "Quantum theory was founded by Max Planck."),
        ("Erwin Schrodinger", "Austria", "Schrodinger equation formulation", "The wave equation was formulated by Erwin Schrodinger."),
        ("Werner Heisenberg", "Germany", "Uncertainty Principle formulation", "The Uncertainty Principle was formulated by Werner Heisenberg."),
        ("Gregor Mendel", "Austria", "experiments on pea plants", "Pea plant experiments were conducted by Gregor Mendel."),
        ("Carl Linnaeus", "Sweden", "system of binomial nomenclature", "Binomial nomenclature was created by Carl Linnaeus."),
        ("Alfred Nobel", "Sweden", "invention of dynamite", "Dynamite was invented by Alfred Nobel in 1867."),
    ]
    
    for i, (scientist, birthplace, achievement, desc) in enumerate(science_subjects):
        idx = 4 + len(subjects) + i
        if idx > 50:
            break
        difficulty = "easy" if idx % 3 == 0 else ("medium" if idx % 3 == 1 else "hard")
        examples.append({
            "qid": f"q{idx}",
            "difficulty": difficulty,
            "question": f"In which country was the scientist who accomplished the {achievement} born?",
            "gold_answer": birthplace,
            "context": [
                {"title": achievement, "text": desc},
                {"title": scientist, "text": f"{scientist} was a scientist born in {birthplace}."}
            ]
        })
        
    print(f"Generated {len(examples)} examples.")
    
    # Save to data/hotpot_100.json
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    out_file = data_dir / "hotpot_100.json"
    out_file.write_text(json.dumps(examples, indent=2), encoding="utf-8")
    print(f"Saved to {out_file}")

if __name__ == "__main__":
    main()
