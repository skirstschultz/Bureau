# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:25:52 2023

@author: Sen
"""
import Bureau


class UserInterface:
    def __init__(self, bureau, files, agent_handler):
        self.bureau = bureau
        self.files = files
        self.agent_handler = agent_handler   
    
    def dashboard_summary(self):
       # Placeholder data
       summary_data = {
           'Total Agents': 10,
           'Active Agents': 5,
           'Inactive Agents': 5,
           'Total Projects': 3,
           'Open Projects': 2,
           'Closed Projects': 1,
           # ... (other summary data)
       }
       return summary_data

    def dashboard_summary_preview(self):
       summary_data = self.dashboard_summary()
       print("Dashboard Summary:")
       print(f"Total Agents: {summary_data['Total Agents']}")
       print(f"Active Agents: {summary_data['Active Agents']}")
       print(f"Inactive Agents: {summary_data['Inactive Agents']}")
       print(f"Total Projects: {summary_data['Total Projects']}")
       print(f"Open Projects: {summary_data['Open Projects']}")
       print(f"Closed Projects: {summary_data['Closed Projects']}")
       # ... (display other summary data)
       
    #Main Menu
    def main_menu(self):
        self.dashboard_summary_preview()  # Display summary preview at the start
        while True:
            print("Main Menu (Landing Page):")
            print("0. Exit")
            print("1. Dashboard")
            print("2. Ask a question of an expert agent")
            print("3. Start a conference call")
            print("4. View Bureau")
            print("5. Manage Agents / AgentHandler")
            print("6. View Metrics / Files")
            print("7. Settings & Information")

            while True:  # Nested loop to keep prompting until a valid choice is made
                choice = input("Enter your choice: ").strip()
                if choice.isdigit() and 0 <= int(choice) <= 7:  # Check if input is a valid number
                    break  # Exit the nested loop once a valid choice is entered
                else:
                    print("Invalid choice. Please enter a number between 0 and 7.")

                if choice == "0":
                    print("Exiting. Have a great day!")
                    break  # Exit the program
                elif choice == "1":
                    self.dashboard_menu()
                elif choice == "2":
                    self.ask_question_menu()
                elif choice == "3":
                    self.start_conference_call_menu()
                elif choice == "4":
                    self.view_bureau_menu()
                elif choice == "5":
                    self.manage_agents_menu()
                elif choice == "6":
                    self.view_metrics_files_menu()
                elif choice == "7":
                    self.settings_information_menu()
                else:
                    print("Invalid choice. Please choose a valid option.")
                
        # To start the UI:
ui = UserInterface()
ui.main_menu()

class Menus:
    def __init__(self, bureau, files, agent_handler):
        self.bureau = bureau
        self.files = files
        self.agent_handler = agent_handler 
        
    # 1. Dashboard
    def dashboard(self):
        while True:
            print("Dashboard:")
            print("1.1 Basic Summary")
            print("0. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "0":
                break  # Back to main menu
            elif choice == "1.1":
                self.basic_summary()
            else:
                print("Invalid choice. Please choose a valid option.")

    def basic_summary(self):
        print("Basic Summary:")  # Placeholder
        # ... (code to display basic summary)
        input("Press Enter to return to Dashboard")
        self.dashboard()
        
    # 2. Ask a Question
    def ask_question_menu(self):
        while True:
            print("2. Ask a question of an expert agent")
            print("2.1 Select an agent")
            print("2.2 Build Question [Question steps]")
            print("2.3 Optional Parameters")
            print("2.4 Queue questions")
            print("2.5 Reset to Default")
            print("2.0 Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "2.0":
                break  # Back to main menu
            elif choice == "2.1":
                self.select_agent()
            elif choice == "2.2":
                self.build_question_menu()
            elif choice == "2.3":
                self.optional_parameters_menu()
            elif choice == "2.4":
                self.queue_questions()
            elif choice == "2.5":
                self.reset_to_default()
            else:
                print("Invalid choice. Please choose a valid option.")
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
    def build_question_menu(self):
        print("2.2.1 (Guiding menu to help craft a perfect prompt)")
        # ... (code to guide user in crafting a perfect prompt)
        input("Press Enter to return")
        self.ask_question_menu()

    def optional_parameters_menu(self):
        print("2.3.1 (Additional Specific Options)")
        # ... (code to handle optional parameters)
        input("Press Enter to return")
        self.ask_question_menu()
# 3. Conference Call
    def start_conference_call_menu(self):
        while True:
            print("3. Start a conference call")
            print("3.1 Quickstart")
            print("3.2 Configure Call")
            print("3.3 Set Agenda")
            print("3.4 Open Conference Call UI")
            print("3.0 Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "3.0":
                break  # Back to main menu
            elif choice == "3.1":
                self.quickstart_menu()
            elif choice == "3.2":
                self.configure_call_menu()
            elif choice == "3.3":
                self.set_agenda_menu()
            elif choice == "3.4":
                self.open_conference_call_ui()
            else:
                print("Invalid choice. Please choose a valid option.")

    def quickstart_menu(self):
        print("3.1.1 Invite Agent(s) (Selection menu of total agents)")
        # ... (code to handle quickstart menu)
        input("Press Enter to return")
        self.start_conference_call_menu()

    def configure_call_menu(self):
        print("3.2.1 Select agents")
        print("3.2.2 Question / Query / Goal")
        print("3.2.3 Call Length (Time for session, Optional)")
        print("3.2.4 Title (Optional)")
        print("3.2.5 Description (Optional)")
        print("3.2.6 Privacy Level (Optional)")
        # ... (code to handle configuring call)
        input("Press Enter to return")
        self.start_conference_call_menu()

    def set_agenda_menu(self):
        print("3.3.1 (Agenda Structuring Options)")
        # ... (code to handle setting agenda)
        input("Press Enter to return")
        self.start_conference_call_menu()
   
# 4. Bureau   
    def view_bureau_menu(self):
        while True:
            print("4. View Bureau")
            print("4.1 Agents")
            print("4.2 Teams")
            print("4.3 Projects")
            print("4.0 Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "4.0":
                break  # Back to main menu
            elif choice == "4.1":
                self.agents_menu()
            elif choice == "4.2":
                self.teams_menu()
            elif choice == "4.3":
                self.projects_menu()
            else:
                print("Invalid choice. Please choose a valid option.")
    #4.1 Agents
    def agents_menu(self):
        print("4.1.1 Agent Search")
        print("4.1.2 View Agent Configurations")
        print("4.1.3 List all agents")
        print("4.1.4 List active agents")
        print("4.1.5 List inactive agents")
        print("4.1.6 Add new agent")
        print("4.1.7 Info on Agents")
        print("4.1.8 Delete Agent (With Confirmation)")
        # ... (code to handle agents submenu)
        input("Press Enter to return")
        self.view_bureau_menu()
    #4.2 Teams
    def teams_menu(self):
        print("4.2.1 List all teams")
        print("4.2.2 List active teams")
        print("4.2.3 List inactive teams")
        print("4.2.4 Search Teams")
        print("4.2.5 Add New Team")
        print("4.2.6 Info on Teams")
        print("4.2.7 Delete Team (With Confirmation)")
        # ... (code to handle teams submenu)
        input("Press Enter to return")
        self.view_bureau_menu()
    #4.3 Projects
    def projects_menu(self):
        print("4.3.1 List all projects")
        print("4.3.2 List active projects")
        print("4.3.3 List inactive projects")
        print("4.3.4 Search Projects")
        print("4.3.5 Add New Project")
        print("4.3.6 Info on Projects")
        print("4.3.7 Delete Project (With Confirmation)")
        # ... (code to handle projects submenu)
        input("Press Enter to return")
        self.view_bureau_menu()
# 5. AgentHandler
    def manage_agents_menu(self):
        while True:
            print("5. Manage Agents / AgentHandler")
            print("5.1 View agent details")
            print("5.2 Update agent information")
            print("5.3 Update agent parameters")
            print("5.4 Remove an agent")
            print("5.5 Un-assign an agent from a team")
            print("5.0 Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "5.0":
                break  # Back to main menu
            elif choice == "5.1":
                self.view_agent_details_menu()
            elif choice == "5.2":
                self.update_agent_information()
            elif choice == "5.3":
                self.update_agent_parameters()
            elif choice == "5.4":
                self.remove_agent()
            elif choice == "5.5":
                self.unassign_agent_from_team()
            else:
                print("Invalid choice. Please choose a valid option.")
                
    def view_agent_details_menu(self):
        print("5.1.1 (Summary Report on Agent)")
        # ... (code to display agent details)
        input("Press Enter to return")
        self.manage_agents_menu()
# 6. View Files / Metrics and Analytics
    def view_metrics_files_menu(self):
        while True:
            print("6. View Metrics / Files")
            print("6.1 View agent metrics")
            print("6.2 View bureau metrics")
            print("6.3 Query metrics")
            print("6.4 Export metrics (Placeholder, with a note about reconsidering this option)")
            print("6.0 Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "6.0":
                break  # Back to main menu
            elif choice == "6.1":
                self.view_agent_metrics_menu()
            elif choice == "6.2":
                self.view_bureau_metrics_menu()
            elif choice == "6.3":
                self.query_metrics_menu()
            elif choice == "6.4":
                self.export_metrics()  # Placeholder method for exporting metrics, as you reconsider this option
            else:
                print("Invalid choice. Please choose a valid option.")

    def view_agent_metrics_menu(self):
        print("6.1.1 (Specific Metrics Viewing Options)")
        # ... (code to view agent metrics)
        input("Press Enter to return")
        self.view_metrics_files_menu()

    def view_bureau_metrics_menu(self):
        print("6.2.1 (Specific Metrics Viewing Options)")
        # ... (code to view bureau metrics)
        input("Press Enter to return")
        self.view_metrics_files_menu()

    def query_metrics_menu(self):
        print("6.3.1 (Specific Querying Options)")
        # ... (code to query metrics)
        input("Press Enter to return")
        self.view_metrics_files_menu()      
    def export_metrics(self):  # Placeholder, still considering/ understanding this option - maybe once logging is built out. or dash.
        print("(Placeholder for exporting metrics)")
        # ... (code to export metrics)
        input("Press Enter to return")
        self.view_metrics_files_menu()
        
    # 7. Settings & Information Menu
    def settings_and_information_menu(self):
        while True:
            print("7. Settings & Information")
            print("7.1 Information")
            print("7.2 Config")
            print("7.3 History")
            print("7.4 Documentation")
            print("7.0 Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "7.0":
                break  # Back to main menu
            elif choice == "7.1":
                self.information_menu()
            elif choice == "7.2":
                self.config_menu()
            elif choice == "7.3":
                self.history_menu()
            elif choice == "7.4":
                self.documentation_menu()
            else:
                print("Invalid choice. Please choose a valid option.")

    def information_menu(self):
        print("7.1.1 (Default Configs Overview)")
        print("7.1.2 (Global Variables Defined)")
        # ... (code to show information)
        input("Press Enter to return")
        self.settings_and_information_menu()

    def config_menu(self):
        print("7.2.1 (Modify Values)")
        print("7.2.2 (Save Presets or 'user_default')")
        # ... (code to configure settings)
        input("Press Enter to return")
        self.settings_and_information_menu()

    def history_menu(self):
        print("7.3.1 (Past Queries and Replies)")
        # ... (code to show history)
        input("Press Enter to return")
        self.settings_and_information_menu()

    def documentation_menu(self):
        print("7.4.1 (GitHub Documentation Link)")
        # ... (code to link to documentation)
        input("Press Enter to return")
        self.settings_and_information_menu()
    
    def query_metrics(self):
        pass
    
#Other Functions 

    def search_for_agent(self):
        # Placeholder method for searching for a specific agent
        pass

    def view_agent_configs(self):
        # Placeholder method for viewing agent configurations
        pass

    def create_new_call(self):
        # Placeholder method for creating a new conference call
        #asks for defintiions then passes start_conference_call method.
        pass

    def view_past_calls(self):
        # Placeholder method for viewing past conference calls
        pass

    def view_call_details(self):
        # Placeholder method for viewing details of a specific conference call
        pass

    def list_all_agents(self):
        print("Listing all agents:")
        # ... (code to list all agents)
        input("Press Enter to return")
        self.view_bureau_menu()

    def list_active_agents(self):
        print("Listing active agents:")
        # ... (code to list active agents)
        input("Press Enter to return")
        self.view_bureau_menu()

    def list_inactive_agents(self):
        print("Listing inactive agents:")
        # ... (code to list inactive agents)
        input("Press Enter to return")
        self.view_bureau_menu()

    def add_new_agent(self):
        print("Adding new agent:")
        # ... (code to add new agent)
        input("Press Enter to return")
        self.view_bureau_menu()

    def delete_agent(self):
        print("Deleting agent:")
        # ... (code to delete agent)
        input("Press Enter to return")
        self.view_bureau_menu()

    # Similar methods can be created for teams and projects based on the menu structure
    # ... (additional methods for teams and projects)

    def update_agent_information(self):
        print("Updating agent information:")
        # ... (code to update agent information)
        input("Press Enter to return")
        self.manage_agents_menu()

    def remove_agent(self):
        print("Removing agent:")
        # ... (code to remove agent)
        input("Press Enter to return")
        self.manage_agents_menu()

    def view_agent_metrics(self):
        print("Viewing agent metrics:")
        # ... (code to view agent metrics)
        input("Press Enter to return")
        self.view_metrics_files_menu()

    def view_bureau_metrics(self):
        print("Viewing bureau metrics:")
        # ... (code to view bureau metrics)
        input("Press Enter to return")
        self.view_metrics_files_menu()

def main():
    bureau = Bureau.Bureau()  # Create an instance of the Bureau class
    files = Bureau.Files()  # Create an instance of the Files class
    agent_handler = Bureau.AgentHandler()  # Create an instance of the AgentHandler class
    
    menus = Menus(bureau, files, agent_handler)
    menus.main_menu()  # Start at the main menu with a small preview/summary of the dashboard

if __name__ == "__main__":
        main()
    
