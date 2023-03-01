import streamlit as st

def main():
    st.set_page_config(page_title="Privacy Policy", layout="wide")
    hide_streamlit_style = """
                    <style>

                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}

                    </style>
                    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    margins_css = """
            <style>
                .main > div {
                    padding-top: 10px;
                }
            </style>
        """

    st.write(margins_css, unsafe_allow_html=True)
    st.title("Privacy Policy")

    st.write("Our Sentiment Analysis App (Wateen Sentify) collects and processes user comments on Facebook pages to provide sentiment analysis. We take your privacy and data security very seriously and have implemented measures to ensure your data is handled responsibly and in accordance with data protection laws.")

    st.header("Collection of Personal Information")
    st.write("When you use our App, we may collect personal information such as your Facebook name and profile picture. We only collect personal information necessary to provide the App's services. We do not collect sensitive personal information, such as your address or financial details.")

    st.header("Collection of Comment Data")
    st.write("The App will collect user comments on Facebook pages, which will be used to provide sentiment analysis. This data will be anonymised and aggregated to maintain user privacy.")

    st.header("Use of Personal Information ")
    st.write("We will only use your personal information to provide the App's services. We will not share your personal information with any third party, except when required by law.")

    st.header("Use of Comment Data")
    st.write("The App will use comment data to provide sentiment analysis. This data will be anonymised and aggregated to maintain user privacy. We will not share comment data with any third party, except when required by law.")

    st.header("Data Security")
    st.write("We take data security seriously and have implemented measures to protect your data from unauthorised access, use, or disclosure. We use secure servers and encryption protocols to protect your data.")

    st.header("Third-Party Services")
    st.write("The App uses third-party services, such as Facebook's API, to provide its services. These services may collect additional data, such as your IP address, to offer their services. We do not control these third-party services and are not responsible for their privacy policies or practices.")

    st.header("User Consent")
    st.write("By using the App, you consent to the collection and use of your personal information and comment data in accordance with this Privacy Policy.")

    st.header("Changes to Privacy Policy")
    st.write("We reserve the right to change this Privacy Policy at any time. Any changes will be posted on this page, and we encourage you to review this Privacy Policy periodically.")


if __name__ == '__main__':
    main()
