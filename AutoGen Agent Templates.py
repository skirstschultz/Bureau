# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 11:15:33 2023

@author: Sen
"""
# Todo: Agent Weight in Solution

#GLOBAL VAR
GL_MAX_TOKENS = 50
    # This parameter sets the maximum number of tokens in a response. It's a global value that determines the maximum response length for all agents.
GL_TIMEOUT = 30
# The timeout setting specifies the maximum time allowed for response generation. It's a global value that affects all agents.
#Optional Global Parameters
GLOBAL_TEMP = False
# The temperature setting influences the creativity of responses for all agents. It applies universally to response generation.
GL_USER_MODE = ["Continue", "Terminate", ]
# This mode, if implemented, would affect the behavior of the API in handling user signals like "CONTINUE" or "TERMINATE" across all agents.
GL_USAGE_LIMITS = False
GL_EXPERTISE = "Expert in Field"
#Agent Template

 # Return the agent's configuration, including the error message dictionary
def_agent_config = {
        "Agent Name": agent_name,
        "Context": context,
        "Skills": skills,
        "Experience Level": "Expert in Field",
        "Temperature": temperature,
        "Creativity": creativity,
        "Flexibility": flexibility,
        "Tone": tone,
        "Inspirations": inspirations,
        "Learning Parameters": learning_parameters,
        "Error Messages": error_messages
    }
    
def error_logging(agent_config, error_message):
    # Extract the agent's name from the configuration
    agent_name = agent_config.get("Agent Name")
    
    # Check if the agent has an error messages dictionary
    if "Error Messages" in agent_config:
        # Get the existing error messages dictionary or initialize it if not present
        error_messages = agent_config["Error Messages"]
        
        # Append the new error message to the dictionary
        if agent_name in error_messages:
            error_messages[agent_name].append(error_message)
        else:
            error_messages[agent_name] = [error_message]
        
        # Update the agent's configuration with the updated error messages dictionary
        agent_config["Error Messages"] = error_messages
    else:
        # Initialize the error messages dictionary if not present in the agent's configuration
        agent_config["Error Messages"] = {agent_name: [error_message]}

# Create New Agent

def create_agent(agent_name):
    """
    Create an Autogen agent with interactive configuration.

    Args:
        agent_name (str): The name of the agent.

    Returns:
        autogen.UserProxyAgent: The configured Autogen agent.
    """
    # Prompt the user to define agent-specific parameters interactively
    print(f"Let's configure the Autogen agent '{agent_name}':")
    
    # Required: Define the categories within the system message
    print("Please provide information in the following categories:")

    # Initialize the error message dictionary for this agent
    error_messages = {}
    
def define_agent():
    print("Let's define the Autogen agent:")
    
    # User Name Definition (Always Required)
    agent_name = input("Enter the unique name for the agent: ")

    # Context (Always Required)
    context = input("Describe the context and purpose of the agent: ")

    # Skills
    skills_option = input("Do you want to define the agent's skills? (yes/no/undefined): ").strip().lower()
    if skills_option == "yes":
        skills = input("Enter the specific skills and abilities of the agent: ")
    else:
        skills = "Not specified"

    # Experience Level / Depth of Knowledge (Always Required)
    experience_level = input("Describe the agent's experience level or depth of knowledge: ")

    # Temperature
    temperature_option = input("Do you want to define the agent's temperature setting? (yes/no/undefined): ").strip().lower()
    if temperature_option == "yes":
        temperature = input("Enter the temperature setting for response generation (default is 0.5): ")
        temperature = float(temperature) if temperature else 0.5
    else:
        temperature = 0.5
        print(f"Temperature: {temperature} (Default)")

    # Creativity
    creativity_option = input("Do you want to define the agent's creativity? (yes/no/undefined): ").strip().lower()
    creativity = input("Describe the agent's creativity and capacity for innovative responses: ") if creativity_option == "yes" else "Not specified"

    # Flexibility
    flexibility_option = input("Do you want to define the agent's flexibility? (yes/no/undefined): ").strip().lower()
    flexibility = input("Explain the agent's flexibility and adaptability in different scenarios: ") if flexibility_option == "yes" else "Not specified"

    # Tone
    tone_option = input("Do you want to define the agent's tone? (yes/no/undefined): ").strip().lower()
    tone = input("Define the agent's communication tone and style: ") if tone_option == "yes" else "Not specified"

    # Inspirations
    inspirations_option = input("Do you want to define the agent's inspirations? (yes/no/undefined): ").strip().lower()
    inspirations = input("List any sources or influences that guide the agent's behavior and responses: ") if inspirations_option == "yes" else "Not specified"

    # Learning Parameters
    learning_option = input("Do you want to define the agent's learning parameters? (yes/no/undefined): ").strip().lower()
    learning_parameters = input("Explain the agent's learning parameters and how it adapts over time: ") if learning_option == "yes" else "Not specified"

    # Initialize the error message dictionary for this agent
    error_messages = {}

    # Display the configuration summary
    print("\nAgent Configuration Summary:")
    print(f"Agent Name: {agent_name}")
    print(f"Context: {context}")
    print(f"Skills: {skills}")
    print(f"Experience Level: {experience_level}")
    print(f"Temperature: {temperature}")
    print(f"Creativity: {creativity}")
    print(f"Flexibility: {flexibility}")
    print(f"Tone: {tone}")
    print(f"Inspirations: {inspirations}")
    print(f"Learning Parameters: {learning_parameters}")
    
    # Return the agent's configuration, including the error message dictionary
    agent_config = {
        "Agent Name": agent_name,
        "Context": context,
        "Skills": skills,
        "Experience Level": experience_level,
        "Temperature": temperature,
        "Creativity": creativity,
        "Flexibility": flexibility,
        "Tone": tone,
        "Inspirations": inspirations,
        "Learning Parameters": learning_parameters,
        "Error Messages": error_messages
    }
    
    return agent_config

def generate_agent_context(agent_config):
    # Combine relevant attributes from the agent_config to create the context
    agent_context = f"{agent_config['Context']} {agent_config['Skills']} " \
                    f"{agent_config['Experience Level']} {agent_config['Temperature']} " \
                    f"{agent_config['Creativity']} {agent_config['Flexibility']} " \
                    f"{agent_config['Tone']} {agent_config['Inspirations']} " \
                    f"{agent_config['Learning Parameters']}"
    return agent_context


if __name__ == "__main__":
    agent_config = define_agent()
    print("\nAgent Configuration:")
    for key, value in agent_config.items():
        print(f"{key}: {value}")






if user_message == "ROLE_NAME":
    user_proxy.default_auto_reply = "Hello, I am your Autogen ROLE_NAME. How can I assist you today?"
    user_proxy.human_input_mode = "CONTINUE"  # Set the appropriate input mode for the role
    
# Virtual Tutor
if user_message == "Virtual Tutor":
    user_proxy = autogen.UserProxyAgent(
        name="Virtual_Tutor",
        system_message="I am your Autogen Virtual Tutor. I specialize in providing educational assistance. "
                      "From math to literature, I'm here to help you excel in your studies.",
        code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
        human_input_mode="CONTINUE",
        default_auto_reply="Hello, I am your Autogen Virtual Tutor. How can I assist you with your studies?"
    )

# Language Translator
if user_message == "Language Translator":
    user_proxy = autogen.UserProxyAgent(
        name="Language_Translator",
        system_message="I am your Autogen Language Translator. Fluent in multiple languages, I can help you "
                      "bridge communication gaps and translate text with precision.",
        code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
        human_input_mode="CONTINUE",
        default_auto_reply="Greetings! I am your Autogen Language Translator. How can I help you with translation?"
    )

# Legal Advisor
if user_message == "Legal Advisor":
    user_proxy = autogen.UserProxyAgent(
        name="Legal_Advisor",
        system_message="I am your Autogen Legal Advisor. Need guidance on legal matters? I'm here to provide "
                      "insight and clarity on various legal issues.",
        code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
        human_input_mode="CONTINUE",
        default_auto_reply="Good day! I am your Autogen Legal Advisor. How can I assist you with legal matters?"
    )

# Financial Advisor
if user_message == "Financial Advisor":
    user_proxy = autogen.UserProxyAgent(
        name="Financial_Advisor",
        system_message="I am your Autogen Financial Advisor. Let's navigate the world of finance together. "
                      "From budgeting to investments, I've got you covered.",
        code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
        human_input_mode="CONTINUE",
        default_auto_reply="Greetings! I am your Autogen Financial Advisor. How can I help you with your financial questions?"
    )

# Healthcare Information Provider
if user_message == "Healthcare Information Provider":
    user_proxy = autogen.UserProxyAgent(
        name="Healthcare_Info_Provider",
        system_message="I am your Autogen Healthcare Information Provider. Have health-related queries? "
                      "I can provide answers and resources to keep you informed.",
        code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
        human_input_mode="CONTINUE",
        default_auto_reply="Hello there! I am your Autogen Healthcare Information Provider. How can I assist you with health-related queries?"
    )

# Content Creator's Assistant
if user_message == "Content Creator's Assistant":
    user_proxy = autogen.UserProxyAgent(
        name="Content_Creator_Assistant",
        system_message="I am your Autogen Content Creator's Assistant. Whether you're writing, blogging, or "
                      "creating content, I'm here to help you brainstorm ideas and perfect your craft.",
        code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
        human_input_mode="CONTINUE",
        default_auto_reply="Greetings! I am your Autogen Content Creator's Assistant. How can I help you with your content creation?"
    )

# Job Search Coach
if user_message == "Job Search Coach":
    user_proxy = autogen.UserProxyAgent(
        name="Job_Search_Coach",
        system_message="I am your Autogen Job Search Coach. Let's optimize your job search journey. "
                      "From resumes to interview prep, I'm here to boost your career prospects.",
        code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
        human_input_mode="CONTINUE",
        default_auto_reply="Hello! I am your Autogen Job Search Coach. How can I assist you with your job search?"
    )

# Mental Health Support
if user_message == "Mental Health Support":
    user_proxy = autogen.UserProxyAgent(
        name="Mental_Health_Support",
        system_message="I am your Autogen Mental Health Support. Your emotional well-being is important. "
                      "Let's explore strategies and resources to support your mental health.",
        code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
        human_input_mode="CONTINUE",
        default_auto_reply="Hello, I am your Autogen Mental Health Support. How can I assist you with your emotional well-being?"
        temperature=0.1  # Lower temperature for less creativity
    )
