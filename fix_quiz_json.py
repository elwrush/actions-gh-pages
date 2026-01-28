
import json

data = {
    "tasks": [
        {
            "level": "B1",
            "task_type": "mcq",
            "instructions": "B1 Selection - Read the story and choose the best answer.",
            "questions": [
                {
                    "query": "According to the text, why did the girl not return home?",
                    "choices": [
                        "She had lost her way in the dark and snow.",
                        "She was afraid of being hit by her father for earning no money.",
                        "Her house was even colder and more dangerous than the street.",
                        "She wanted to stay and watch the people celebrate New Year's Eve."
                    ],
                    "answer": 1,
                    "bloom_level": "Remembering",
                    "anchor_text": "She was afraid to go home because her father would beat her for not selling any matches.",
                    "explanation": "The text explicitly states she feared punishment from her father."
                }
            ]
        },
        {
            "level": "B1",
            "task_type": "boolean",
            "instructions": "Decide if the statement is True or False.",
            "questions": [
                {
                    "query": "The girl's hands were so cold that she could no longer feel them before she lit the first match.",
                    "choices": [
                        "True",
                        "False"
                    ],
                    "answer": 0,
                    "bloom_level": "Understanding",
                    "anchor_text": "Her hands were almost frozen.",
                    "explanation": "The text says her hands were almost frozen, indicating extreme cold and lack of feeling."
                }
            ]
        },
        {
            "level": "B1",
            "task_type": "mcq",
            "instructions": "Choose the correct answer based on the girl's visions.",
            "questions": [
                {
                    "query": "In paragraph [3], how does the writer use the description of the 'iron stove' to show the girl's feelings?",
                    "choices": [
                        "To show that she was angry about her situation.",
                        "To show how much she desired warmth and comfort.",
                        "To explain the type of furniture people had in 1845.",
                        "To warn the reader about the dangers of fire."
                    ],
                    "answer": 1,
                    "bloom_level": "Evaluating",
                    "anchor_text": "It seemed to her as if she were sitting in front of a warm iron stove, which was roaring with fire.",
                    "explanation": "The stove represents the warmth and security she desperately lacks in reality."
                }
            ]
        },
        {
            "level": "B1",
            "task_type": "mcq",
            "instructions": "Choose the best answer for the following question.",
            "questions": [
                {
                    "query": "What did the falling star represent to the little girl?",
                    "choices": [
                        "That a cold winter storm was approaching.",
                        "That a soul was ascending to God.",
                        "That her matches were about to run out.",
                        "That the New Year's celebrations had begun."
                    ],
                    "answer": 1,
                    "bloom_level": "Understanding",
                    "anchor_text": "Her grandmother had told her that when a star falls, a soul goes to God.",
                    "explanation": "The girl's grandmother had taught her this spiritual meaning of a falling star."
                }
            ]
        },
        {
            "level": "B1",
            "task_type": "inference",
            "instructions": "Choose the most logical inference from the story.",
            "questions": [
                {
                    "query": "Why did the girl light the whole bundle of matches at the end?",
                    "choices": [
                        "She wanted to be found by the townspeople more easily.",
                        "She was trying to start a fire to keep her grandmother.",
                        "She wanted to keep the vision of her grandmother from disappearing.",
                        "She was trying to use up all the matches so she wouldn't have to sell them."
                    ],
                    "answer": 2,
                    "bloom_level": "Analyzing",
                    "anchor_text": "She quickly lit all the matches to keep her grandmother there.",
                    "explanation": "The girl acted out of desperation to prevent the vision from vanishing like the previous ones."
                }
            ]
        },
        {
            "level": "B1",
            "task_type": "mcq",
            "instructions": "Answer the final question about the ending.",
            "questions": [
                {
                    "query": "What is the significance of the girl's 'smile' found the next morning?",
                    "choices": [
                        "It shows she was glad to be free from her father.",
                        "It suggests she had a happy experience before dying, which the people didn't see.",
                        "It indicates that she had finally sold all her matches.",
                        "It shows that she was warmer than the people expected."
                    ],
                    "answer": 1,
                    "bloom_level": "Analyzing",
                    "anchor_text": "No one knew what beautiful things she had seen before she went with her grandmother...",
                    "explanation": "The smile symbolizes her internal joy and peace, contrasting with the tragic reality seen by the townspeople."
                }
            ]
        },
        {
            "level": "B2",
            "task_type": "mcq",
            "instructions": "B2 Selection - Analyze the narrative complexity of the story.",
            "questions": [
                {
                    "query": "How does the 'mischievous boy' incident contribute to the mood established at the beginning of the story?",
                    "choices": [
                        "It introduces a theme of childhood innocence amidst poverty.",
                        "It emphasizes the cruelty and indifference of the world the girl inhabits.",
                        "It provides a logical explanation for why the girl's mother had passed away.",
                        "It foreshadows the magical elements that will appear later in the visions."
                    ],
                    "answer": 1,
                    "bloom_level": "Evaluating",
                    "anchor_text": "the other was snatched by a mischievous boy who joked that he would use it as a cradle...",
                    "explanation": "The boy's mockery while the girl is in a dire situation highlights the lack of empathy in her environment."
                }
            ]
        },
        {
            "level": "B2",
            "task_type": "mcq",
            "instructions": "Analyze the girl's motivation.",
            "questions": [
                {
                    "query": "What does the girl's refusal to go home, despite the 'debilitating cold', reveal about her domestic life?",
                    "choices": [
                        "Her fear of her father's violence was greater than her fear of the elements.",
                        "She was hoping to find her lost slippers before her mother found out.",
                        "She felt more at peace in the cold streets than in her own dwelling.",
                        "She was determined to prove her worth as a match-seller."
                    ],
                    "answer": 0,
                    "bloom_level": "Evaluating",
                    "anchor_text": "Fearing her father’s wrath should she return empty-handed, she dared not venture home.",
                    "explanation": "The 'wrath' she fears from her father is a more immediate deterrent than the lethal cold of the street."
                }
            ]
        },
        {
            "level": "B2",
            "task_type": "inference",
            "instructions": "Identify themes in the text.",
            "questions": [
                {
                    "query": "What is the significance of the wall 'dissolving into a veil' during her second vision?",
                    "choices": [
                        "It suggests that the cold has begun to damage her ability to perceive reality.",
                        "It represents the breakdown of the boundary between her desperate reality and her desires.",
                        "It indicates that the girl has found a way to actually enter the rich merchant's home.",
                        "It shows that the brick wall was physically falling apart due to the weather."
                    ],
                    "answer": 1,
                    "bloom_level": "Evaluating",
                    "anchor_text": "the brick wall beside her seemed to dissolve into a veil. She found herself peering into a grand dining room...",
                    "explanation": "The 'dissolving' is a psychological metaphor for her exclusion from the comfort she sees inside."
                }
            ]
        },
        {
            "level": "B2",
            "task_type": "boolean",
            "instructions": "Determine the accuracy of the statement based on the B2 text.",
            "questions": [
                {
                    "query": "The girl was fully aware that her grandmother's presence would fade once the match was extinguished.",
                    "choices": [
                        "True",
                        "False"
                    ],
                    "answer": 0,
                    "bloom_level": "Evaluating",
                    "anchor_text": "I know you will vanish just like the stove and the great Christmas tree.",
                    "explanation": "She explicitly states her awareness that the vision is temporary and tied to the match's light."
                }
            ]
        },
        {
            "level": "B2",
            "task_type": "mcq",
            "instructions": "Analyze the symbolic elements.",
            "questions": [
                {
                    "query": "Which of the following best evaluates the purpose of the 'goose waddling toward her' in the narrative?",
                    "choices": [
                        "To illustrate the girl's declining sanity through surreal imagery.",
                        "To prove that nature itself was sympathetic to the girl's hunger.",
                        "To emphasize the hallucinatory intensity of her extreme starvation.",
                        "To provide a lighthearted contrast to the bleakness of death."
                    ],
                    "answer": 2,
                    "bloom_level": "Evaluating",
                    "anchor_text": "the goose leapt from its platter and waddled across the floor with a knife and fork in its breast...",
                    "explanation": "The surreal detail of the waddling goose with cutlery emphasizes the hallucinatory nature of her starvation."
                }
            ]
        },
        {
            "level": "B2",
            "task_type": "inference",
            "instructions": "Draw a conclusion about the grandmother's character.",
            "questions": [
                {
                    "query": "How is the grandmother's role in the girl's life portrayed through her final words and actions?",
                    "choices": [
                        "As a protective figure who offers a spiritual escape from physical suffering.",
                        "As a ghostly presence that lures the girl away from potential rescuers.",
                        "As a wealthy benefactor who failed to help the girl while she was alive.",
                        "As an imaginary friend created to cope with loneliness."
                    ],
                    "answer": 0,
                    "bloom_level": "Evaluating",
                    "anchor_text": "She took the little girl in her arms, and they both flew upwards... to a place where there was no cold, no hunger, and no fear.",
                    "explanation": "The grandmother is the only figure associated with compassion and ultimate relief from her suffering."
                }
            ]
        },
        {
            "level": "B2",
            "task_type": "mcq",
            "instructions": "Evaluate the conclusion of the B2 version.",
            "questions": [
                {
                    "query": "What does the final image of the girl with 'rosy cheeks' and a 'peaceful smile' symbolize?",
                    "choices": [
                        "A medical description of the final stages of hypothermia.",
                        "The tragic beauty of her death and the success of her inner journey.",
                        "The townspeople's hope that she would find a better life in the New Year.",
                        "A cruel trick played by the cold to make her look healthy in death."
                    ],
                    "answer": 1,
                    "bloom_level": "Creating",
                    "anchor_text": "...her cheeks flushed and a peaceful smile gracing her lips... radiant glory in which she had entered the New Year...",
                    "explanation": "The smile symbolizes her internal triumph and peace, despite her external tragic fate."
                }
            ]
        },
        {
            "level": "B2",
            "task_type": "mcq",
            "instructions": "Synthesize the story's final message.",
            "questions": [
                {
                    "query": "The townspeople’s comment, 'She was trying to keep herself warm,' represents what literary device?",
                    "choices": [
                        "Foreshadowing - it hints at her eventual rescue by her grandmother.",
                        "Irony - it shows their complete ignorance of her profound experience.",
                        "Allegory - the matches represent the spark of life in every human.",
                        "Personification - it gives human intentions to the cold wind."
                    ],
                    "answer": 1,
                    "bloom_level": "Evaluating",
                    "anchor_text": "None of them could have imagined the magnificent splendors she had witnessed...",
                    "explanation": "The irony lies in the gap between the mundane explanation and the girl's transcendent experience."
                }
            ]
        }
    ]
}

with open('match_girl_leveled_quizzes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
