# Scam-Detector: Phase 2 Demo MVP Pipeline (Vertical with Feedback Loop)

```mermaid
flowchart TB
    %% Vertical Demo MVP Pipeline with Feedback
    subgraph Demo_Pipeline["Phase 2: Demo MVP"]
        style Demo_Pipeline fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
        
        %% Agents Layer
        subgraph Agents["Agents Layer"]
            A1["Collect Data (CSV/JSON/API)"] --> A2["Extract Metadata: author, timestamp, source"]
            A2 --> A3["Preprocess Text: clean, normalize, tokenize"]
            A3 --> B1
        end
        
        %% AI/ML Layer
        subgraph AI["AI/ML Layer"]
            B1["Predict Fake / Real / Suspicious"] --> B2["Generate Credibility Score 0-100"]
            B2 --> B3["Output: Label + Score"]
            B3 --> C1
        end
        
        %% Blockchain Layer
        subgraph Blockchain["Blockchain Layer"]
            C1["Hash Article + Score + Timestamp"] --> C2["Store on Blockchain (immutable)"]
            C2 --> C3["Output: Blockchain Transaction ID"]
            C3 --> D1
        end
        
        %% Dashboard / Alert Layer
        subgraph Dashboard["Dashboard / Alert System"]
            D1["Show Article"] --> D2["Display Prediction + Score + Blockchain Status"]
            D2 --> D3["Optional: Color-coded Alerts Info/Warning/Critical"]
            D3 --> D4["Output: Visual Alert to User / Feedback Collection"]
            D4 --> B1["Feedback Loop: User / Analyst Feedback"]
        end
    end
