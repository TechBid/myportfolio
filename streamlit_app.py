import streamlit as st

st.set_page_config(layout="wide")

st.title("🧠 Federated Learning with Blockchain & IPFS")

st.header("📌 Project Overview")
st.markdown("""
This project integrates **Federated Learning (FL)** with **Blockchain** and **IPFS** to create a decentralized, auditable, and transparent AI training ecosystem. The system ensures that local data from different clients (e.g., stores, hospitals, IoT devices) remains private, while model updates are aggregated securely on a central node. Each aggregation round is recorded on the Ethereum blockchain for transparency, and the aggregated global model is stored on IPFS for decentralized access.
""")

st.header("⚙️ System Architecture")
st.image("BlockchainAI.png", caption="System Diagram")

st.subheader("1. Clients (Local Nodes)")
st.markdown("""
- Each client (Raspberry Pi or Jetson Nano device) trains a local ML/DL model using its private data.
- Frameworks used: TensorFlow, Scikit-learn, Docker, FastAPI, Flask.
- Example: **Client A Prediction System (Store A)**
    - URL: [Store A Prediction System](https://mainstore-rjmb.onrender.com/)
    - Input data is used locally to predict outcomes and retrain Store A’s local models.
""")

st.subheader("2. Central Server (Aggregator Node)")
st.markdown("""
- Runs **Flower (FL framework)** for model aggregation.
- OS: Windows/Linux.
- Automation via Task Scheduler / Cron jobs.
- Collects model weights, aggregates them, and produces a global model.
""")

st.subheader("3. IPFS Storage")
st.markdown("""
- The global model is saved to IPFS after each aggregation.
- An **IPFS content hash** is generated to ensure immutability and integrity.
""")

st.subheader("4. Ethereum Blockchain Logging")
st.markdown("""
- Each training round’s metadata (accuracy, timestamp, round number, IPFS hash) is recorded on the **Ethereum Sepolia testnet**.
- Example Transaction (Round 10): [Sepolia Transaction on Etherscan](https://sepolia.etherscan.io/tx/0x008a3ef87cb15c2490b8e3029a356812b217e8c2e49389c62945eb125a25722a)
""")

st.subheader("5. Dashboard & Visualization")
st.markdown("""
- A **Streamlit Dashboard** visualizes metrics such as:
    - Global accuracy trends
    - Node-specific accuracy contributions
    - Blockchain transaction logs
- URL: [Federated System Dashboard](https://fedsysdashboard.onrender.com/)
- 📊 Observation: **Global accuracy improves with increased training rounds**, showing the positive impact of collaboration.
""")

st.header("📂 Data Flow Example")
st.markdown("""
1.  **Client A (Store A)** submits input data to its prediction system.
2.  Local model predicts output and updates its parameters.
3.  Model weights are sent to the central aggregator (not raw data).
4.  Aggregator combines weights from all clients → generates a global model.
5.  Global model stored on IPFS + metadata logged to blockchain.
6.  Dashboard updates global accuracy & blockchain records.
7.  Improved model sent back to clients for further training → cycle continues.
""")

st.header("🛠️ Frameworks & Tools Used")
st.markdown("""
- **Machine Learning**: TensorFlow, Scikit-learn
- **Federated Learning**: Flower (FL framework)
- **Web Apps (Client-side)**: FastAPI, Flask, Dockerized deployment
- **Blockchain & Storage**: Ethereum Sepolia testnet, Hardhat + Web3.py for smart contract & transactions, IPFS for decentralized model storage
- **Dashboards**: Streamlit (real-time monitoring)
- **Hardware (Client Nodes)**: Raspberry Pi, NVIDIA Jetson Nano
""")

st.header("🔗 Useful Links")
st.markdown("""
- **Store A Prediction System**: [https://mainstore-rjmb.onrender.com/](https://mainstore-rjmb.onrender.com/)
- **Dashboard for Metrics**: [https://fedsysdashboard.onrender.com/](https://fedsysdashboard.onrender.com/)
- **Sample Blockchain Transaction (Round 10)**: [Etherscan Link](https://sepolia.etherscan.io/tx/0x008a3ef87cb15c2490b8e3029a356812b217e8c2e49389c62945eb125a25722a)
- **Store A - Prediction API Endpoint**: [https://federatedsys.onrender.com/fed_sys](https://federatedsys.onrender.com/fed_sys)
- **Store A - API Documentation**: [View API Docs](#)
""")

st.header("📖 Documentation")
st.markdown("""
- **Federated Learning (Flower):** [https://flower.dev](https://flower.dev)
- **Ethereum Sepolia Testnet:** [Sepolia Docs](https://ethereum.org/en/developers/docs/networks/sepolia/)
- **IPFS Protocol:** [https://ipfs.tech](https://ipfs.tech)
- **Streamlit Dashboards:** [https://streamlit.io](https://streamlit.io)
""")

st.header("🌟 Key Contributions of This System")
st.markdown("""
1.  **Data Privacy** – Local training ensures raw data never leaves the client.
2.  **Transparency** – Blockchain records provide immutable proof of training rounds.
3.  **Integrity** – Models stored on IPFS with unique hashes for verification.
4.  **Scalability** – Supports multiple clients/nodes with lightweight devices.
5.  **Improved Accuracy** – Collaborative training boosts overall model performance.
""")

st.header("Linear Walkthrough")
st.markdown("""
1.  **Local data and prediction (Client side)**: Each client (Store A, Store B, Store C) collects and stores its own data locally. This data never leaves the client in raw form. Each client runs a local prediction service (a small app on a Raspberry Pi / Jetson / server). The service: accepts input (user form or sensor data), uses the client’s local model to return a prediction, and optionally stores the new training example locally for later training. Clients prepare local training datasets from their own stored examples (preprocessing, normalization, etc.). Output at this stage: updated local dataset and the client’s local model parameters (weights) after local updates.
2.  **Local training (per client)**: At scheduled intervals or on demand, each client trains its local model on its own data (one or more local epochs). Training produces an updated set of model parameters (the numerical “weights” and bias values). The client packages only the model update (the weights and metadata such as number of samples) — not the original data — for transmission. Output at this stage: a model-update artifact (weights + sample count + client ID).
3.  **Communication to the aggregator (server)**: Clients send their model-update artifacts to the central aggregator (the device/server in your chassis). This happens over the network (secure channel/VPN). The aggregator collects updates from all participating clients for the current round. Artifacts transmitted: client ID, weights, num_samples, optional local metrics (accuracy/loss).
4.  **Aggregation (server / Flower)**: The aggregator runs the federated-learning coordinator (Flower) which: receives all client updates for the round, performs a weighted aggregation (e.g., FedAvg) using sample counts to compute the new global model weights, optionally evaluates the aggregated model on a validation dataset. The aggregated model is finalized for that round. Output at this stage: global_model_round_N — the aggregated model weights.
5.  **Persisting the global model (server)**: The server saves the aggregated model to disk in a designated folder (e.g., global_models/global_round_N.h5). This saved file is the exact binary representation of the global model at that round. Artifact created: saved model file per round.
6.  **Decentralized storage (IPFS)**: The server uploads the saved model file to IPFS (or a pinning service). IPFS returns a content identifier (CID / IPFS hash) that uniquely fingerprints that file. Optionally the server pins the file so it remains available on the IPFS network. Output at this stage: ipfs_hash for the aggregated model.
7.  **On-chain audit (blockchain)**: The server prepares a small metadata record for the round: e.g., round number, global accuracy, per-node accuracies, timestamp, notes, and the ipfs_hash. The server submits a transaction to the private/public blockchain (e.g., Sepolia testnet) that writes or emits this metadata using a smart contract. The blockchain processes the transaction and returns a transaction ID (tx hash / block reference) once confirmed. Output at this stage: blockchain transaction ID that proves the model file and metadata were recorded at a particular time.
8.  **Off-chain ledger (coordinator)**: The server appends or updates an off-chain ledger (a JSON file or database) with the round’s full entry: round number, timestamp, global accuracy, node accuracies, ipfs_hash, and the on-chain block_tx. This ledger is the immediate source for dashboards and quick lookups. Artifact created: ledger.json or DB record for the round.
9.  **Dashboard & monitoring**: The Streamlit dashboard reads the ledger and/or queries the blockchain and IPFS to display: global accuracy trend by round, per-client contributions and accuracies, IPFS hash and a link to the model file, blockchain transaction IDs with links to Etherscan (or explorer). Stakeholders can visually verify model improvement and click through to the blockchain or IPFS for audit. Visible effects: charts, tables, and links showing provenance and performance.
10. **Model distribution back to clients**: The server makes the latest global model available to clients (push or clients fetch). Options: Push: server sends the new weights to each client automatically. Pull: clients periodically check the server or GitHub/IPFS and download the latest model. Each client updates its local model with the new global weights and resumes local training/prediction. Result: clients start the next round from the improved global model.
11. **Optional: Continuous integration (GitHub / Render / Flask)**: The server can optionally upload each saved global model to a GitHub repo (or cloud storage). Web apps (hosted on Render) can fetch the latest model from GitHub/IPFS and use it for live predictions or extra fine-tuning on user input. This ties your FL cycle into web endpoints for external users. Benefit: easy distribution and history tracking of model files.
12. **Audit & verification loop (how an auditor checks)**: Auditor reads the ledger entry for a round and gets the ipfs_hash and block_tx. Auditor fetches the model from IPFS using the ipfs_hash and computes its fingerprint. Auditor verifies the on-chain record (transaction & event) matches the ipfs_hash and timestamp. Auditor can reproduce metrics by loading the model and running a validation dataset if permitted. Outcome: verifiable proof that the model existed and was recorded at that time.
""")

st.header("Practical notes, risks and recommended practices")
st.markdown("""
- **Privacy**: raw client data never leaves clients. Only model updates are transmitted.
- **Availability**: ensure IPFS pinning or cloud backup so model files remain retrievable.
- **Key management**: protect the private key used to sign blockchain transactions. Use environment secrets or hardware keys for production.
- **Audit batching**: to improve throughput, consider uploading and recording on-chain every N rounds (checkpointing) instead of every round.
- **Monitoring**: log times for local training, communication, aggregation, IPFS upload, and tx confirmation to measure rounds/minute and spot bottlenecks.
- **Resilience**: handle clients dropping out; strategy should tolerate missing updates and proceed when minimum clients respond.
""")

st.header("Quick linear summary")
st.markdown("""
1.  Clients train locally and produce weight updates.
2.  Clients send updates to the central aggregator.
3.  Aggregator performs FedAvg to create the global model.
4.  Aggregated model is saved to disk.
5.  Saved model is uploaded to IPFS → returns ipfs_hash.
6.  Aggregation metadata + ipfs_hash is recorded on the blockchain → returns block_tx.
7.  Ledger is updated and dashboard published.
8.  Clients fetch or receive the new global model → next round begins.
""")