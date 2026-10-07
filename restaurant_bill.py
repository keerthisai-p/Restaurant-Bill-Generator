import streamlit as st

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Restaurant Bill Generator",
    page_icon="🍽️",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(
            135deg,
            #dbeafe,
            #c4b5fd,
            #ddd6fe,
            #bfdbfe
        );
        background-size: 400% 400%;
        animation: smoothGradient 12s ease infinite;
    }

    @keyframes smoothGradient {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }

    .main-title {
        text-align: center;
        color: #355c4a;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #6d7c75;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .bill-box {
        background: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0px 5px 20px rgba(70, 90, 80, 0.10);
        margin-top: 20px;
    }

    .total-box {
        background: #e8f4ed;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
    }

    .grand-total {
        color: #285943;
        font-size: 32px;
        font-weight: bold;
    }

    .section-title {
        color: #355c4a;
        font-size: 23px;
        font-weight: 600;
        margin-top: 10px;
    }

    .footer {
        text-align: center;
        color: #82918a;
        margin-top: 35px;
        font-size: 14px;
    }

    div[data-testid="stButton"] > button {
        background-color: #8fb9a5;
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
    }

    div[data-testid="stButton"] > button:hover {
        background-color: #6f9e89;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- RESTAURANT MENU ----------------
menu = {
    "🍕 Margherita Pizza": 220,
    "🍔 Veg Burger": 150,
    "🍝 White Sauce Pasta": 180,
    "🥪 Grilled Sandwich": 120,
    "🍜 Veg Noodles": 160,
    "🍛 Paneer Biryani": 240,
    "🥗 Fresh Salad": 100,
    "🍟 French Fries": 90,
    "🥤 Cold Drink": 60,
    "🍰 Chocolate Cake": 130,
    "☕ Coffee": 70,
    "🍦 Ice Cream": 80
}

# ---------------- HEADER ----------------
st.markdown(
    '<div class="main-title">🍽️ Restaurant Bill Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Select your favorite dishes and generate your bill</div>',
    unsafe_allow_html=True
)

# ---------------- CUSTOMER DETAILS ----------------
st.markdown(
    '<div class="section-title">👤 Customer Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    customer_name = st.text_input(
        "Customer Name",
        placeholder="Enter your name"
    )

with col2:
    table_number = st.text_input(
        "Table Number",
        placeholder="Enter table number"
    )

st.markdown("---")

# ---------------- FOOD SELECTION ----------------
st.markdown(
    '<div class="section-title">🍴 Select Food Items</div>',
    unsafe_allow_html=True
)

selected_items = []

for item, price in menu.items():

    col1, col2, col3 = st.columns([3, 1.5, 1.5])

    with col1:
        selected = st.checkbox(
            f"{item} — ₹{price}",
            key=f"select_{item}"
        )

    with col2:
        quantity = st.number_input(
            "Qty",
            min_value=1,
            max_value=20,
            value=1,
            step=1,
            key=f"qty_{item}",
            disabled=not selected
        )

    with col3:
        if selected:
            item_total = price * quantity
            st.write(f"₹{item_total}")

            selected_items.append(
                (item, price, quantity, item_total)
            )

# ---------------- BILL CALCULATION ----------------
st.markdown("---")

st.markdown(
    '<div class="section-title">🧾 Bill Summary</div>',
    unsafe_allow_html=True
)

if selected_items:

    subtotal = sum(item[3] for item in selected_items)

    # ---------------- TAX AND DISCOUNT ----------------
    col1, col2 = st.columns(2)

    with col1:
        tax_percent = st.number_input(
            "GST / Tax (%)",
            min_value=0.0,
            max_value=30.0,
            value=5.0,
            step=0.5
        )

    with col2:
        discount_percent = st.number_input(
            "Discount (%)",
            min_value=0.0,
            max_value=50.0,
            value=0.0,
            step=1.0
        )

    discount_amount = subtotal * discount_percent / 100
    taxable_amount = subtotal - discount_amount
    tax_amount = taxable_amount * tax_percent / 100
    grand_total = taxable_amount + tax_amount

    # ---------------- BILL ----------------
    st.markdown(
        '<div class="bill-box">',
        unsafe_allow_html=True
    )

    st.markdown("### 🧾 Your Restaurant Bill")

    if customer_name:
        st.write(f"**Customer:** {customer_name}")

    if table_number:
        st.write(f"**Table:** {table_number}")

    st.markdown("---")

    # ---------------- BILL HEADER ----------------
    h1, h2, h3, h4 = st.columns([3, 1, 1.5, 1.5])

    with h1:
        st.markdown("**Item**")

    with h2:
        st.markdown("**Qty**")

    with h3:
        st.markdown("**Price**")

    with h4:
        st.markdown("**Total**")

    # ---------------- BILL ITEMS ----------------
    for item, price, quantity, item_total in selected_items:

        c1, c2, c3, c4 = st.columns([3, 1, 1.5, 1.5])

        with c1:
            st.write(item)

        with c2:
            st.write(quantity)

        with c3:
            st.write(f"₹{price}")

        with c4:
            st.write(f"₹{item_total}")

    st.markdown("---")

    # ---------------- SUBTOTAL ----------------
    c1, c2 = st.columns([3, 1])

    with c1:
        st.write("**Subtotal**")

    with c2:
        st.write(f"**₹{subtotal:.2f}**")

    # ---------------- DISCOUNT ----------------
    if discount_percent > 0:

        c1, c2 = st.columns([3, 1])

        with c1:
            st.write(
                f"Discount ({discount_percent:.1f}%)"
            )

        with c2:
            st.write(
                f"- ₹{discount_amount:.2f}"
            )

    # ---------------- TAX ----------------
    c1, c2 = st.columns([3, 1])

    with c1:
        st.write(
            f"GST / Tax ({tax_percent:.1f}%)"
        )

    with c2:
        st.write(
            f"+ ₹{tax_amount:.2f}"
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    # ---------------- GRAND TOTAL ----------------
    st.markdown(
        f"""
        <div class="total-box">
            <div style="font-size:18px; color:#60756b;">
                GRAND TOTAL
            </div>
            <div class="grand-total">
                ₹{grand_total:.2f}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- PAYMENT ----------------
    st.markdown("### 💳 Payment Method")

    payment_method = st.radio(
        "Choose payment method",
        ["💵 Cash", "💳 Card", "📱 UPI"],
        horizontal=True
    )

    st.success(
        f"Payment Method: {payment_method}"
    )

    # ---------------- COMPLETE ORDER ----------------
    if st.button(
        "✅ Complete Order",
        use_container_width=True
    ):

        st.success(
            f"🎉 Thank you "
            f"{customer_name if customer_name else 'Customer'}! "
            f"Your order has been placed successfully."
        )

else:

    st.info(
        "🍴 Please select at least one food item to generate your bill."
    )

# ---------------- FOOTER ----------------
st.markdown(
    '<div class="footer">Thank you for dining with us! ❤️</div>',
    unsafe_allow_html=True
)