class TeamModel():
    def getData(self):
        team = [
            {
                "institution": "Paul Scherrer Institute",
                "people": [
                    {
                        "name": "Dr. Chris Mutel",
                        "role": "Research scientist, PI of OASES",
                        "img": "chris_mutel.jpg",
                        "descr": 'Chris is professionally and personally committed to making sustainability \
                        information more available, robust, and understandable. To this end, he builds open tools and \
                        data management strategies, and researches the role of spatial and temporal scale in LCA. \
                        He is the lead developer of the <a href="https://brightway.dev/" target="_blank">Brightway LCA</a> \
                        software toolkit, chair of <a href="https://bonsai.uno/" target="_blank">BONSAI</a>, and blogs \
                        <a href="https://chris.mutel.org/" target="_blank">here</a> about the technical details of LCA.'

                    },
                    {
                        "name": "Christian Bauer",
                        "role": "Research scientist",
                        "img": "christian_bauer.jpg",
                        "descr": 'Christian coordinates the LCA activities within the \
                        <a href="https://www.psi.ch/en/ta" target="_blank">Technology Assessment Group</a> at \
                        PSI. He has been working there since 2003, primarily focusing on Life Cycle and Sustainability \
                        Assessment of current and future energy systems, mobility technologies and fuel supply \
                        processes. He is member of the board of the ecoinvent association.'
                    },
                    {
                        "name": "Aleksandra Kim",
                        "role": "Doctoral student",
                        "img": "aleksandra_kim.jpg",
                        "descr": "In her doctoral work Aleksandra addresses \
                        the issue of uncertainties and data quality in life cycle inventories by utilising Sensitivity \
                        Analysis and Uncertainty Quantification techniques. She is also interested in statistical \
                        tools for data analysis in LCA, algorithms and efficient computations. In the scope of the \
                        OASES project, her primary focus lies in integrated sustainability assessment of Swiss consumption."
                     }
                ]
            },
            {
                "institution": "University of Freiburg",
                "people": [
                    {
                        "name": "Prof. Dr. Stefan Pauliuk",
                        "role": 'Head of Industrial Ecology Group',
                        "img": "stefan_pauliuk.jpg",
                        "descr": 'Stefan is an expert in sustainable development strategies. His work includes supply \
                        chain analysis, scenario modelling for sustainable material futures, and indicator development \
                        for resource efficiency and circular economy strategies. Together with colleagues he estimated \
                        current in-use stocks of steel and developed scenarios for material efficiency in the future \
                        steel cycle that show the substantial greenhouse gas emissions mitigation potential of material \
                        efficiency.'
                    },
                    {
                        "name": "Arthur Jakobs",
                        "role": "Doctoral student",
                        "img": "arthur_jakobs.jpg",
                        "descr": "Arthur's work focuses on a first principles approach to the hybridisation of LCA \
                        data and environmentally extended input output models. With his background in statistical \
                        modelling in astrophysics, he has a strong interest in the uncertainty in the models currently \
                        employed in industrial ecology and as such the uncertainty in hybrid LCA models."
                    },
                ]
            },
            {
                "institution": "Empa",
                "people": [
                    {
                        "name": "Dr. Patrick Waeger",
                        "role": "Head of Technology & Society Laboratory",
                        "img": "patrick_waeger.jpg",
                        "descr": 'Patrick has background in chemistry, philosophy and sociology. After his doctoral \
                        thesis in environmental sciences at ETH Zürich, he worked as an environmental consultant and \
                        later joined Empa. Currently, he is the head of Empa’s \
                        <a href="www.empa.ch/tsl" target="_blank">Technology & Society Laboratory</a>, \
                        which explores the potentials and limitations of novel materials and \
                        emerging technologies to support transitions to a more sustainable society, with a focus on \
                        the analysis and evaluation of material and energy stocks and flows.'
                    },
                    {
                        "name": "Dr. Roland Hischier",
                        "role": "Head of the Advancing LCA Group",
                        "img": "roland_hischier.jpg",
                        "descr": "Roland is the Head of the Advancing LCA Group within the Technology & Society \
                        Laboratory at Empa. He holds a PhD from ETH Zürich. After having spent 3 years in the ecology \
                        department of a private company, he joined Empa in the beginning of 2000. As an LCA specialist,\
                         he was involved in numerous LCA studies dealing mainly with ICT, mobility and nanotechnology. \
                         He is currently the president of the board of ecoinvent, having contributed to its content \
                         and management for almost 20 years."
                    },
                    {
                        "name": "Marcus Berr",
                        "role": "Doctoral student",
                        "img": "marcus_berr.jpg",
                        "descr": '"We cannot solve our problems with the same thinking we used when we created them." \
                        (Albert Einstein). Having this in mind, Marcus is pleased to contribute to the creation of \
                        knowledge for achieving an environmentally friendly and sustainable economy and society. \
                        Within his work package of OASES, he assesses supply risks along global Swiss supply chains \
                        to be able to provide solutions for a more sustainable supply of goods and services.'
                    },
                ]
            },
            {
                "institution": "Ecoinvent",
                "people": [
                    {
                        "name": "Dr. Gregor Wernet",
                        "role": "Executive director",
                        "img": "gregor_wernet.jpg",
                        "descr": "Gregor is the executive director of ecoinvent and has been involved with it since 2005.\
                         He is also the editor for chemicals and pharmaceuticals. Originally hailing from Germany, \
                         he has a PhD in chemistry from ETH Zurich.  Gregor has been heavily involved in the \
                         development of ecoinvent version 3.  He maintains a tight network with all actors of the \
                         LCA fields, from government to NGOs to industrial associations."
                    },
                    {
                        "name": "Dr. Guillaume Bourgault",
                        "role": "Project Manager",
                        "img": "guillaume_bourgault.jpg",
                        "descr": "Guillaume has a strong background in chemical engineering and LCA. His doctoral \
                        thesis focused on uncertainty issues emerging at the interface of inventory and impact \
                        assessment. At ecoinvent he supports the team in scientific programming, makes sure that \
                        information flows smoothly between data suppliers, clients, licensees, impact assessment \
                        and software developers. He runs database-wide assessment to ensure consistency and rigor."
                    },
                ]
            }
        ]

        data = {
            "team" : team
        }
        return data




modelTeam = TeamModel()
