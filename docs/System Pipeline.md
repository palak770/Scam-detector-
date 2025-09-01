# Scam-Detector: System Pipeline

```mermaid
flowchart TD
    %% Full Phase 1 Conceptual Pipeline
    subgraph Full_Pipeline["Phase 1: Full Conceptual Pipeline"]
        P1["Data Collection Layer"] --> P2["Preprocessing & Privacy Layer"]
        P2 --> P3["AI & NLP Engine"]
        P3 --> P4["Fact Verification Module"]
        P4 --> P5["Correlation & Scoring Engine"]
        P5 --> P6["Human-in-the-loop Review"]
        P6 --> P7["Alerting System"]
        P3 --> P8["CV / Deepfake Detection"]
        P3 --> P9["ASR / Audio Analysis"]
        P4 --> P10["Blockchain Ledger + Crypto Rewards"]
    end

    %% Demo-Focused Pipeline
    subgraph Demo_Pipeline["Phase 2: Demo MVP"]
        style Demo_Pipeline fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
        
        subgraph Agents["Agents Layer"]
            A1["Collect Data (CSV/JSON/API)"] --> A2["Extract Metadata: author, timestamp, source"]
            A2 --> A3["Preprocess Text: clean, normalize, tokenize"]
            A3 --> B
        end
        
        subgraph AI["AI/ML Layer"]
            B1["Predict Fake / Real / Suspicious"] --> B2["Generate Credibility Score 0-100"]
            B2 --> C
        end
        
        subgraph Blockchain["Blockchain Layer"]
            C1["Hash Article + Score + Timestamp"] --> C2["Store on Blockchain (immutable)"]
            C2 --> D
        end
        
        subgraph Dashboard["Dashboard / Alert System"]
            D1["Show Article"] --> D2["Display Prediction + Score + Blockchain Status"]
            D2 --> D3["Optional: Color-coded Alerts Info/Warning/Critical"]
        end
    end

    %% Demo Actions Linked to Full Pipeline
    A1 --> P1
    B1 --> P3
    C1 --> P10
