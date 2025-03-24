import ollama

# Show welcome message
print("🦙 Welcome to LlamaCmd - Your Offline Linux Command Helper! 🦙")
print("💡 Type a command description to get a suggested Linux command.")
print("💡 Type '/exit' at any time to quit.\n")

# Track last suggested command
last_command = None

# Function to load model from file
def load_model_from_file():
    default_model = "llama3"  # Fallback model
    try:
        with open("model.txt", "r") as f:
            model = f.read().strip()
            if model:
                return model
            else:
                return default_model
    except FileNotFoundError:
        return default_model  # Silently default to llama3
    except Exception as e:
        print(f"⚠️ Error reading 'model.txt': {e}. Using default 'llama3'.")
        return default_model

# Load model at startup
current_model = load_model_from_file()  # Fixed: was 'loa', now complete function call
print(f"Using model: {current_model}\n")

# Main loop
while True:
    # Get user input
    command = input("Describe the command you're looking for: ").strip()

    # Handle empty input
    if not command:
        print("⚠️ Please enter a description (or '/exit' to quit)")
        print()
        continue

    # Handle exit request
    if command.lower() == "/exit":
        print("👋 Exiting LlamaCmd... Goodbye!")
        break

    # Get command suggestion from the selected model
    try:
        response = ollama.chat(
            model=current_model,
            messages=[{"role": "user", "content": f"Give me a single executable Linux command for {command}, no explanation, just the command, or 'unsure' if unclear"}]
        )
        suggested_command = response.get("message", {}).get("content", "").strip().split("\n")[0]
    except Exception as e:
        print(f"⚠️ Error fetching command: {e}")
        continue

    # Space output
    print()

    # Show result or unsure message
    if not suggested_command or suggested_command.lower() == "unsure":
        print("⚠️ Model is unsure, try a clearer command.")
    else:
        print(f"🤖 Suggested command: {suggested_command} 🚀")
        last_command = suggested_command
        
        # Prompt for details or exit
        detail_choice = input("Details? (y/n) or /exit: ").strip().lower()
        if detail_choice == "/exit":
            print("👋 Exiting LlamaCmd... Goodbye!")
            break
        elif detail_choice == "y":
            # Prompt for specific question
            question = input(f"What do you want to know about '{last_command}'? ").strip()
            
            # Handle exit request at any stage
            if question.lower() == "/exit":
                print("👋 Exiting LlamaCmd... Goodbye!")
                break
            
            # Only ask AI if question isn’t empty
            try:
                if question:
                    response = ollama.chat(
                        model=current_model,
                        messages=[{"role": "user", "content": f"Explain: {question} about the Linux command {last_command}"}]
                    )
                else:
                    response = ollama.chat(
                        model=current_model,
                        messages=[{"role": "user", "content": f"Provide a short explanation of the Linux command: {last_command}"}]
                    )

                # Print explanation
                explanation = response.get("message", {}).get("content", "").strip()
                print(f"\n🤔 Details: {explanation}\n")
            except Exception as e:
                print(f"⚠️ Error fetching explanation: {e}")

    # Space output
    print()