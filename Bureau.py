# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 12:14:38 2023
Classes: Bureau, ConferenceRoom w/ Facilitator Agent(user proxy?), AgentHandler
@author: Sen
"""
#Prereq Software

# Create VENV

#Pip install
#-pip install pyautogen pymemgpt
#install requirements.txt
'''
import os
import autogen
import memgpt.autogen.memgpt_agent as memgpt_autogen
import memgpt.autogen.interface as autogen_interface
import memgpt.agent as agent       
import memgpt.system as system
import memgpt.utils as utils 
import memgpt.presets as presets
import memgpt.constants as constants 
import memgpt.personas.personas as personas
import memgpt.humans.humans as humans
from memgpt.persistence_manager import InMemoryStateManager, InMemoryStateManagerWithPreloadedArchivalMemory, InMemoryStateManagerWithEmbeddings, InMemoryStateManagerWithFaiss
import openai
'''
import datetime
from collections import defaultdict




#CONFIGS
config_list = [
    {
        "api_type": "open_ai",
        "api_base": "https://TO BE EDITED-5001.proxy.runpod.net/v1",
        "api_key": "NULL",
    },
]

llm_config = {"config_list": config_list, "seed": 42}

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




class Bureau:
    def __init__(self):
        self.agents = {}
        self.all_agents = {}  # Dictionary to hold all agents and their configs
        self.agent_usage = defaultdict(lambda: {
            'usage_count': 0,
            'token_count': 0,
            'last_used': None,
            'task_completion_rate': 0,
            'error_rate': 0,
            'error_messages': [],
            'user_prompts': 0,
            'call_prompts': 0
        })
        self.cross_functional_teams = {}
        self.user_proxy = None  # To be set using set_facilitator method

    def update_agent_usage(self, agent_name, tokens_used=0):
        self.agent_usage[agent_name]['usage_count'] += 1
        self.agent_usage[agent_name]['token_count'] += tokens_used
        self.agent_usage[agent_name]['last_used'] = datetime.datetime.now()

    def mark_inactive_agents(self):
        two_weeks_ago = datetime.datetime.now() - datetime.timedelta(weeks=2)
        for agent_name, metrics in self.agent_usage.items():
            if metrics['last_used'] < two_weeks_ago:
                self.all_agents[agent_name]['status'] = 'inactive'

    def get_active_agents(self):
        return {k: v for k, v in self.all_agents.items() if v.get('status') == 'active'}

    def get_inactive_agents(self):
        return {k: v for k, v in self.all_agents.items() if v.get('status') == 'inactive'}

    def create_cf_team(self, team_name, agents, manager):
        self.cross_functional_teams[team_name] = {
            'Agents': agents,
            'Manager': manager,
            'Team Goals': [],
            'Completed Tasks': []
        }

    def set_facilitator(self, user_proxy):
        self.user_proxy = user_proxy

    def hire_agent(self, agent_name, agent_config):
        agent_config['status'] = 'active'  # Setting status to active upon hiring
        self.all_agents[agent_name] = agent_config  # Adding agent to all_agents

    def fire_agent(self, agent_name):
        confirmation = input(f"Are you sure you want to remove {agent_name}? (yes/no): ").lower()
        if confirmation == 'yes':
            self.all_agents.pop(agent_name, None)  # Remove agent from all agents
            print(f"Agent {agent_name} removed.")
        else:
            print(f"Agent {agent_name} not removed.")
            
    def set_global_variable(self, var_name, var_value):
        # Set a global variable
        self.global_vars[var_name] = var_value

    def get_global_variable(self, var_name):
        # Get the value of a global variable
        return self.global_vars.get(var_name, None)
# Create a Bureau instance
bureau = Bureau()
# Create Agent objects for all agents in the Bureau
agents = bureau.create_agents()
        
class AgentHandler:
    def __init__(self):
        self.agents = {}  # A dictionary to hold the agents
        self.bureau = bureau  # Reference to the Bureau instance
    
    def select_agent(self):
        available_agents = self.agent_handler.list_agents()
        if not available_agents:
            print("No agents available.")
            return None  # No agents to select from
        
        print("Select an agent:")
        for index, agent_name in enumerate(available_agents, start=1):
            print(f"{index}. {agent_name}")
        
        while True:
            choice = input("Enter the number of the agent you want to select, or 0 to go back: ").strip()
            if choice.isdigit():
                choice = int(choice)
                if 0 <= choice <= len(available_agents):
                    if choice == 0:
                        return None  # User chose to go back
                    selected_agent_name = available_agents[choice - 1]
                    return selected_agent_name
                else:
                    print("Invalid choice. Please choose a valid option.")
            else:
                print("Invalid input. Please enter a number.")
                
    def define_agent(self, agent_name, context, skills, experience_level, temperature, creativity, flexibility, tone, inspirations, learning_parameters):
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
            "Error Messages": {}
        }
        return agent_config
    
    def generate_context_string(self, agent_name):
        formatted_agent_name = agent_name.lower().replace(" ", "_")
        config_context_string = f'{formatted_agent_name}_config_context'
        return config_context_string

    def generate_agent_context(self, agent_config):
        # Assume that agent_name is an attribute of agent_config or adjust accordingly
        agent_name = agent_config.agent_name  
        # Now call generate_context_string with self and pass agent_name to it
        agent_context = self.generate_context_string(agent_name)  

        
        agent_config_summary_parts = []
        
        # Ensure variables are accessed from agent_config dictionary
        context = agent_config.get('Context', 'Unknown Context')
        skills = agent_config.get('Skills', [])
        experience_level = agent_config.get('Experience Level', 'Unknown Level')
        temperature = agent_config.get('Temperature')
        creativity = agent_config.get('Creativity')
        flexibility = agent_config.get('Flexibility')
        inspirations = agent_config.get('Inspirations', [])
        tone = agent_config.get('Tone')
        learning_parameters = agent_config.get('Learning Parameters', 'Default Parameters')
        error_messages = agent_config.get('Error Messages', [])
        
        agent_config_summary_parts.append(f"This agent, named {agent_name}, is finely honed for operation within the {context} realm.")
        agent_config_summary_parts.append(f"Boasting a skill set encompassing {', '.join(skills)}, it operates at an experience level of {experience_level}.")
        
        if temperature:
           agent_config_summary_parts.append(f"The temperature setting is at {temperature}, balancing the trade-off between exploration and exploitation.")
       
        if creativity:
           agent_config_summary_parts.append(f"The creativity level is set at {creativity}, allowing for a novel approach to problem-solving.")
       
        if flexibility:
           agent_config_summary_parts.append(f"The flexibility score is {flexibility}, ensuring adaptability in a diverse range of situations.")
       
        if inspirations:
           agent_config_summary_parts.append(f"Inspired by {', '.join(inspirations)},")
           
        if tone:    
           agent_config_summary_parts.append(f"the agent's tone is set to {tone}, which complements the interaction dynamics effectively.")
       
        agent_config_summary_parts.append(f"The learning parameters are set to {learning_parameters}, promoting a robust learning curve.")
        agent_config_summary_parts.append(f"In case of errors, it's programmed to respond with predefined messages: {', '.join(error_messages)}.")
       
        agent_config_context_summary = " ".join(agent_config_summary_parts)
        # Now, setting the summary to the agent_config_context
        globals()[agent_context] = agent_config_context_summary
        system_message = self.generate_agent_context(agent_name, agent_config)
        return agent_config_context_summary  # return the summary directly
    
    def generate_system_message(self, agent_name, agent_config):
        agent_config_context = self.generate_context_string(agent_name)
        # Assuming the agent_config dictionary contains all the necessary information
        agent_config_summary_parts = []




# Collaboration with Files/Metrics
# Collaboration with Bureau / List of All
# Tuning of Conferenc Room, Suggestion for prompt / config structure? further out.

class ConferenceRoom:
    def __init__(self, facilitator):
        self.active_agents = []  # List to hold active agents in the conference
        self.facilitator = facilitator  # Facilitator agent for recommendations
        self.authoritative_agent = None  # Agent with the highest weight (authority) in the conference
    
    
    def start_conference_call(self, agents):
        self.active_agents.extend(agents)  # Add agents to the active list
        
        # Facilitator recommends agents based on their expertise or other criteria
        recommended_agents = self.facilitator.recommend_agents(self.active_agents)
        print(f"Recommended agents for the call: {', '.join(recommended_agents)}")
        
        # Confirm the call invites
        confirmation = input("Do you want to proceed with these agents? (yes/no): ").lower()
        if confirmation == 'yes':
            print("Hosting the call...")
            # Host the call (implement your call logic here)
        else:
            print("Call cancelled.")
            self.active_agents = []  # Clear the active agents list
        
        # End call and free memory/resources
        self.active_agents = []  # Clear the active agents list
        
    def set_agenda(self, tasks):
        self.agenda.extend(tasks)  # Add tasks to the agenda
        
    def assign_task(self, agent_name, task):
        agent = self.all_agents.get(agent_name)
        if agent:
            agent.handle_task(task)  # Assumes a method to handle tasks
            self.update_agent_usage(agent_name)  # Update usage metrics
        else:
            print(f"No agent found with name {agent_name}.")

    
    def delegate_tasks(self):
        for task in self.agenda:
            assigned_agent_name = input(f"Who should handle the task '{task}'? (leave blank for facilitator assignment): ")
            if assigned_agent_name:
                assigned_agent = self.all_agents.get(assigned_agent_name)
                if assigned_agent:
                    assigned_agent.assign_task(task)  # Assumes a method to assign tasks
                else:
                    print(f"No agent found with name {assigned_agent_name}.")
            else:
                # Facilitator assignment logic
                suitable_agent = self.find_suitable_agent(task)
                if suitable_agent:
                    suitable_agent.assign_task(task)
        self.agenda.clear()
    def recommend_new_agent(self, task, confidence):
        threshold = 0.75  # Assume a threshold for confidence
        if confidence < threshold:
            print(f"Low confidence ({confidence}) for task '{task}'. Consider assigning a new team or hiring a new agent for better handling.")        
    def end_call(self):
        print("Ending the call...")
        self.active_agents = []  # Clear the active agents list
        self.authoritative_agent = None  # Reset the authoritative agent
        
    def track_metrics(self):
        for agent_name, metrics in self.agent_usage.items():
            print(f"{agent_name}:")
            for metric, value in metrics.items():
                print(f"  {metric}: {value}")
        
    def view_discussion(self):
        # Print or return the discussions, decisions, and collaborations
        # ... your code ... realtime and also afterwards.
        pass  # remove this line once you add your code
    def real_time_feedback(self, feedback):
        # Implement mechanisms for real-time feedback
        # ... your code ...
        pass  # remove this line once you add your code
        
    def agent_weight(self, agent):
        # Define the weight of each agent's influence based on some criteria
        # This is a simplified example, adjust as needed
        expertise_level = agent.get_expertise_level()  # Assume agents have a method to get their expertise level
        influence = expertise_level * 10  # Assume a simple linear relation for this example
        return influence

    # Additional method to set the user_proxy if it's not a part of the facilitator
    def set_facilitator(self, user_proxy):
        self.user_proxy = user_proxy

class Files:
    def __init__(self):
        self.agents_data = {}  # Dictionary to hold metrics for each agent
        self.teams_data = {}  # Dictionary to hold metrics for each team
        self.queries_data = []  # List to hold data for each query
        self.bureau = bureau  # Reference to the Bureau instance
    def log_agent_metrics(self, agent_name, metrics):
        # Log metrics for a specific agent
        self.agents_data[agent_name] = metrics
    
    def log_team_metrics(self, team_name, metrics):
        # Log metrics for a specific team
        self.teams_data[team_name] = metrics
    
    def log_query_data(self, query_data):
        # Log data for a specific query
        self.queries_data.append(query_data)
    
    def list_agents(self):
        # List all agents and their metrics
        for agent_name, metrics in self.agents_data.items():
            print(f"Agent: {agent_name}")
            for metric_name, metric_value in metrics.items():
                print(f"  {metric_name}: {metric_value}")
            print()
    
    def list_teams(self):
        # List all teams and their metrics
        for team_name, metrics in self.teams_data.items():
            print(f"Team: {team_name}")
            for metric_name, metric_value in metrics.items():
                print(f"  {metric_name}: {metric_value}")
            print()
    
    def list_queries(self):
        # List all queries and their data
        for query_index, query_data in enumerate(self.queries_data, 1):
            print(f"Query {query_index}:")
            for key, value in query_data.items():
                print(f"  {key}: {value}")
            print()

    def get_agent_metrics(self, agent_name):
        # Get metrics for a specific agent
        return self.agents_data.get(agent_name, {})

    def get_team_metrics(self, team_name):
        # Get metrics for a specific team
        return self.teams_data.get(team_name, {})
    
    def get_query_data(self, query_index):
        # Get data for a specific query
        try:
            return self.queries_data[query_index]
        except IndexError:
            print(f"No data for query {query_index}")
            return None

     
files = Files(bureau)
