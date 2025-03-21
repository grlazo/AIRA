import streamlit as st
import os
from query_data import query_rag
import base64

def get_pdf_files():
    """Get list of PDF files from the data directory."""
    pdf_files = []
    for file in os.listdir("data"):
        if file.endswith(".pdf"):
            pdf_files.append(file)
    return pdf_files

def display_pdf(pdf_path):
    """Display PDF file in Streamlit."""
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="900" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def parse_sources(response_text):
    """Parse sources from response text."""
    if "Sources:" in response_text:
        response, sources = response_text.split("Sources:", 1)
        sources = sources.strip("[] ").split(", ")
        return response.replace("Response:", "").strip(), sources
    return response_text, []

def main():
    st.set_page_config(page_title="RAG Prompt System", layout="wide")
    
    st.title("AI Research Assistant")
    
    # Create two columns for the layout
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.subheader("Prompt Documents")
        query = st.text_area("Enter your prompt:", height=100)
        
        if st.button("Submit Prompt", type="primary"):
            if query:
                with st.spinner("Processing query..."):
                    try:
                        response = query_rag(query)
                        response_text, sources = parse_sources(response)
                        
                        st.success("Prompt processed successfully!")
                        st.subheader("Response")
                        st.write(response_text)
                        
                        if sources:
                            st.subheader("Sources")
                            for source in sources:
                                # Extract filename and page from source
                                # Format: "data/filename.pdf:page:chunk"
                                parts = source.strip('"').split(":")
                                filename = os.path.basename(parts[0])
                                page = parts[1]
                                st.write(f"- {filename} (Page {page})")
                    except Exception as e:
                        st.error(f"Error processing query: {str(e)}")
            else:
                st.warning("Please enter a query.")
        
        # Display available PDF files
        st.subheader("Available Documents")
        pdf_files = get_pdf_files()
        selected_pdf = st.selectbox("Select a PDF (editable line) :", pdf_files)
        
    with col2:
        st.subheader("Document Viewer")
        if selected_pdf:
            pdf_path = os.path.join("data", selected_pdf)
            display_pdf(pdf_path)
        else:
            st.info("Select a PDF file to view its contents.")

if __name__ == "__main__":
    main()

