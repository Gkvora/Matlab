import streamlit as st # type: ignore
from PIL import Image

def set_page_config():
    """Sets the page configuration.
    """
    st.set_page_config(
        page_title = "Documentation",
        page_icon= Image.open("//sfs.net/bia/BIA_AI/web site/logo.png"),
        layout="wide")
set_page_config()

st.markdown("""<style>
            .text_left{
                text-align: left;
                }
            .text_right{
                text-align: right;
                }
            .text_center{
                text-align: center;
                }
            .font_size_16{
                font-size:16px;
            }
            .font_size_18{
                font-size:18px;
                font-weight: bold;
            }
            .font_size_24{
                font-size:24px;
            }
            .font_size_28{
                font-size:28px;
            }
            .bold_text{
                font-weight: bold;
            }
            .stImage{
                justify-content: center;
                box-shadow: 0px 2px 8px 2px #888888;
            }
            </style>""", unsafe_allow_html=True)

def show_img(file_path):
    """ show image"""
    img = Image.open(file_path)
    st.write(img)

st.markdown("""<p class="text_center bold_text font_size_28">INDEX</p>
            <ul>
                <li>Dashboard
                    <ul>
                        <li><a href="#how_to_use">How To Use</a></li>
                        <li><a href="#report_list">Reports</a></li>
                    </ul>
                </li>
                <li><a href="#cut_redefine">Cut Redefined</a></li>
                <li><a href="#pricing">Pricing</a></li>
            </ul>""", unsafe_allow_html=True)
st.markdown("""<p class="text_center bold_text font_size_28" id="how_to_use">How To Use Dashboard</p>""", unsafe_allow_html=True)
st.markdown("<p class='text_left font_size_16'><b>Login page</b> select Report Type Dashboard and enter your user name & Password. Then check Stay Login.</p>", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\login.png")

st.markdown("<p class='text_left font_size_16'>Select year and month to load data between this crite area.</p>", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\data load filter.png")

st.markdown("<p class='text_left font_size_16'>Select Data Filter To Filter Data for Reports.</p></br>", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\data filter for report.png")

st.markdown("""<p class='text_left font_size_16' id="report_list">In report Selection, we have several reports which listed below.</p>
            <ul>
                <li><a href="#sale_dashboard">Sale Dashboard</a></li>
                <li><a href="#full_stock_report">Full Stock Report</a></li>
                <li><a href="#quick_sale_report">Quick Sale Report</a></li>
                <li><a href="#sale_new_report">Sale/New Arrival Report</a></li>
                <li><a href="#trend_report">Trend Report in %</a></li>
                <li><a href="#inflow_outflow_report">InFlow OutFlow Report</a>
                    <ul>
                        <li><a href="#inflow_outflow">InFlow-OutFlow</a></li>
                        <li><a href="parameter_wise_inflow_outflow">Parameter wise InFlow-OutFlow</a></li>
                    </ul>
                </li>
                <li><a href="#change_in_price">Change in Price (Disc%/PPC)</a>
                    <ul>
                        <li><a href="#compare_two_shape">Compare Two Shape</a></li>
                        <li><a href="#compare_two_shape_sale">Sale%</a></li>
                        <li><a href="#compare_two_shape_by_quick_sale">Compare Two Shape by Quick Sale</a></li>
                    </ul>
                </li>
                <li><a href="#shape_wise_report">Shape wise Report</a></li>
                <li><a href="#zone_wise_sale_report">Zone Wise Sale Report</a></li>
                <li><a href="#sale_per_report">Sale Percentage Report</a></li>
                <li><a href="#sale_proportion_report">Sale Proportion Report</a></li>
                <li><a href="#import_report">Import Report</a></li>
                <li><a href="#heat_map_of_ppc_report">Heat Map of PPC Report</a></li>
                <li><a href="#sale_comparison_report">Sale Comparison Report</a></li>
                <li><a href="#tradescreen">Tradescreen</a></li>
                <li><a href="#stocksummary">Cno1 and Cno.2 Stock summary</a></li>
            </ul>""", unsafe_allow_html=True)

st.markdown("""<p class='text_left font_size_24' id="sale_dashboard"><b>&#8658; Sale Dashboard</b></p>
            <ul>
                <li>Select Report Type to Generate report.</li>
                <li>Select Company1 and 2 to compare.
                    <ul>
                        <li>Company like 1, 2, 7, 9, Rap Net, Manufacturing, None (if you want to see only one company).</li>
                    </ul>
                </li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\sale report filter.png")

st.markdown("""
            <ul>
                <li>It will Show comparison of two company’s.</li>
            </ul>
            <p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report sale dashboard.png")

st.markdown("""
            <ul>
                <li><b>Description</b>
                    <ul>
                        <li><b>Total Revenue:</b> It will show total revenue of selected date crite area.</li>
                        <li><b>Total Sold Crt:</b> It will show total Sold Crt. of selected date crite area.</li>
                        <li><b>Total Sold Pieces:</b> It will show # of Piece of selected date crite area.</li>
                        <li><b>Sold Proportion (New Arrival):</b> It will show total revenue of selected date crite area.</li>
                        <li><b>Sold Proportion (Stock):</b> It will show sale from stock which dose not contain new to sale and new arrival.</li>
                        <li><b>Sold Proportion:</b> It will show sold proportion stock that contain new arrival.</li>
                        <li><b>Sales Cycle Time:</b> It will show sale from new Arrival.</li>
                        <li><b>Round%:</b> It will show percentage of stone type Round in sale.</li>
                        <li><b>Fancy%:</b> It will show percentage of stone type fancy in sale.</li>
                        <li><b>Monthly Growth Rate:</b> It will show percentage of growth up and down from last month.</li>
                        <li><b>Quarterly Growth Rate:</b> It will show percentage of growth up and down from last two month.</li>
                        <li><b>Selected time period Growth Rate:</b> It will show percentage of growth up and down from which selected in data range.</li>
                        <li><b>Round Avg Price:</b> It will show avg price of round sold stones.</li>
                        <li><b>Fancy Avg Price:</b> It will show avg price of Fancy sold stones.</li>
                    </ul>
                </li>
            </ul>""", unsafe_allow_html=True)

st.markdown("""<p class='text_left font_size_24' id="full_stock_report"><b>&#8658; Full Stock Report</b></p>
            <ul>
                <li>Select Current Stone Location (India, USA, UAE, Botswana, Israel, Hongkong, South Africa).</li>
                <li>Select MFG Location (Surat, Southafrica, Namibia, Botswana).</li>
                <li>Select Current Stage of Stone (Stock, Lab, Without Price, Upcoming.</li>
                <li>Select Type for value of Report like (No of Stone, Total Crt, Total Value).</li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\full stock report filter.png")

st.markdown("""
            <ul>
                <li>Report with Group.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report full stock Group.png")

st.markdown("""
            <ul>
                <li>Report with Detail.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report full stock detail.png")

st.markdown("""<p class='text_left font_size_24' id="quick_sale_report"><b>&#8658; Quick Sale Report</b></p>
            <ul>
                <li>Select Report Type to Generate report.</li>
                <li>Select Company1 and 2 to compare.
                    <ul>
                        <li>Company like 1, 2, 7, 9, Rap Net, Manufacturing, None (if you want to see only one company).</li>
                    </ul>
                </li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\quick sale report filter.png")

st.markdown("""
            <ul>
                <li>It will Show comparison of two company’s.</li>
                <li>Cumulatiove Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report quick sale cumulative.png")

st.markdown("""
            <ul>
                <li>Count vise Table.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report quick sale stones.png")

st.markdown("""<p class='text_left font_size_24' id="sale_new_report"><b>&#8658; Sale/New Arrival Report</b></p>
            <ul>
                <li>Select Report Type to Generate report.</li>
                <li>Select Company1 and 2 to compare.
                    <ul>
                        <li>Company like 1, 2, 7, 9, Rap Net, Manufacturing, None (if you want to see only one company).</li>
                    </ul>
                </li>
                <li>Select mode to group and unique data (Daily, Weekly, monthly, Quarter, and Yearly).</li>
                <li>Select Type for value of Report like (No of Stone, Total Crt, Total Value).</li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\sale new report filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report sale new.png")

st.markdown("""<p class='text_left font_size_24' id="trend_report"><b>&#8658; Trend Report in %</b></p>
            <ul>
                <li>Select Report Type to Generate report.</li>
                <li>Select Company1 and 2 to compare.
                    <ul>
                        <li>Company like 1, 2, 7, 9, Rap Net, Manufacturing, None (if you want to see only one company).</li>
                    </ul>
                </li>
                <li>Select mode to group and unique data (Daily, Weekly, monthly, Quarter, and Yearly).</li>
                <li>Select Type for value of Report like (No of Stone, Total Crt, Total Value).</li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\trend report filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report trend.png")

st.markdown("""<p class='text_left font_size_24' id="inflow_outflow_report"><b>&#8658; InFlow OutFlow Report</b></p>
            <ul>
                <li id="inflow_outflow">InFlow-OutFlow
                    <ul>
                        <li>Select report InFlow-OutFlow.</li>
                        <li>Select Company1 and 2 to compare.
                            <ul>
                                <li>Company like 1, 2, 7, 9, Rap Net, Manufacturing, None (if you want to see only one company).</li>
                            </ul>
                        </li>
                        <li>Select Type for value of Report like (No of Stone, Total Crt, Total Value).</li>
                        <li>Select months for inflow outflow report.</li>
                        <li>Click on View Report.</li>
                    </ul>
                </li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\inflow outflow report filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report inflow outflow.png")

st.markdown("""
            <ul>
                <li id="parameter_wise_inflow_outflow">Parameter wise InFlow-OutFlow
                    <ul>
                        <li>Select Report Parameter wise  InFlow-OutFlow.</li>
                        <li>Select Company1 and 2 to compare.
                            <ul>
                                <li>Company like 1, 2, 7, 9, Rap Net, Manufacturing, None (if you want to see only one company).</li>
                            </ul>
                        </li>
                        <li>Select Type for value of Report like (No of Stone, Total Crt, Total Value).</li>
                        <li>Select months for inflow outflow report.</li>
                        <li>Select Params for x axis (Depth,Table,Ratioo,Range).</li>
                        <li>Select Shape for filter data.</li>
                        <li>Click on View Report.</li>
                    </ul>
                </li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\parameter wise inflow outflow report filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report parameter wise inflow outflow.png")

st.markdown("""<p class='text_left font_size_24' id="change_in_price"><b>&#8658; Change in Price (Disc%/PPC)</b></p>
            <ul>
                <li>Select Report Type to Generate report.</li>
                <li>Select Company1 and 2 to compare.
                    <ul>
                        <li>Company like 1, 2, 7, 9, Rap Net, Manufacturing, None (if you want to see only one company).</li>
                    </ul>
                </li>
                <li>Select From Date (start date).</li>
                <li>Select To Date (end date).</li>
                <li>Select mode for diffrence by Dict Per Disc% or by value PPC.</li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\change in price filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report change in price by category.png")
show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report change in price by size.png")
show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report change in price by size count.png")

st.markdown("""<p class='text_left font_size_24' id="shape_wise_report"><b>&#8658; Shape wise Report</b></p>
            <ul>
                <li id="compare_two_shape">Compare Two Shape
                    <ul>
                        <li>Select report Compare Two Shape.</li>
                        <li>Select shape 1 and 2 to compare with each other.</li>
                        <li>Select Company (1, 2, 7, 9, Rap Net, Manufacturing).</li>
                        <li>Select mode to group and unique data (Daily, Weekly, monthly, Quarter, and Yearly).</li>
                        <li>Select status (Sale, New Arrival, Stock).</li>
                        <li>Click on View Report.</li>
                    </ul>
                </li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\compare two shape wise report filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report compare two shape wise.png")

st.markdown("""
            <ul>
                <li id="compare_two_shape_sale">Sale%
                    <ul>
                        <li>Select Company1 and 2 to compare.
                            <ul>
                                <li>Company like 1, 2, 7, 9, Rap Net, Manufacturing, None (if you want to see only one company).</li>
                            </ul>
                        </li>
                        <li>Select x axis to show at X axis.</li>
                        <li>Select parameter axis to show at Y axis.</li>
                        <li>Select mode to group and unique data (Daily, Weekly, monthly, Quarter, and Yearly)..</li>
                        <li>Click on View Report.</li>
                    </ul>
                </li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\sale% shape wise report filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report sale% shape wise.png")


st.markdown("""
            <ul>
                <li id="compare_two_shape_by_quick_sale">Compare Two Shape by Quick Sale
                    <ul>
                        <li>Select shape 1 and 2 to compare with each other.</li>
                        <li>Select Company (1, 2, 7, 9, Rap Net, Manufacturing).</li>
                        <li>Click on View Report.</li>
                    </ul>
                </li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\compare two shape by quick sale filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report compare two shape by quick sale.png")

st.markdown("""<p class='text_left font_size_24' id="zone_wise_sale_report"><b>&#8658; Zone Wise Sale Report</b></p>
            <ul>
                <li>Select Report Type to Generate report.</li>
                <li>Select Company (1, Rap Net).</li>
                <li>Select status (Sale, New Arrival, Stock).</li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\zone wise report filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report zone wise .png")

st.markdown("""<p class='text_left font_size_24' id="sale_per_report"><b>&#8658; Sale Percentage Report</b></p>
            <ul>
                <li>Select Report Type to Generate report.</li>
                <li>Select Company1 and 2 to compare.
                    <ul>
                        <li>Company like 1, 2, 7, 9, Rap Net, Manufacturing, None (if you want to see only one company).</li>
                    </ul>
                </li>
                <li>Select status (Sale, New Arrival, Stock).</li>
                <li>Select Parms (Shape,Range,Color,Purity,FLS,Polish,Cut,SYMM).</li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\sale percentage report filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report sale percentage.png")

st.markdown("""<p class='text_left font_size_24' id="sale_proportion_report"><b>&#8658; Sale Proportion Report</b></p>
            <ul>
                <li>Select Report Type to Generate report.</li>
                <li>Select Company1 and 2 to compare.
                    <ul>
                        <li>Company like 1, 2, 7, 9, Rap Net, Manufacturing, None (if you want to see only one company).</li>
                    </ul>
                </li>
                <li>Select status (Sale, New Arrival, Stock).</li>
                <li>Select Parms (Shape,Range,Color,Purity,FLS,Polish,Cut,SYMM).</li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\sale proportion report filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report sale proportion.png")

st.markdown("""<p class='text_left font_size_24' id="import_report"><b>&#8658; Import Report</b></p>
            <ul>
                <li>Select mode to group and unique data (Daily, Weekly, monthly, Quarter, and Yearly.</li>
                <li>Select Type for value of Report like (No of Stone, Total Crt, Total Value).</li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\import report filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\import report.png")

st.markdown("""<p class='text_left font_size_24' id="heat_map_of_ppc_report"><b>&#8658; Heat Map of PPC Report</b></p>
            <ul>
                <li>Select Company1 and 2 to compare.
                    <ul>
                        <li>Company like 1, 2, 7, 9, Rap Net, Manufacturing, None (if you want to see only one company).</li>
                    </ul>
                </li>
                <li>Select Range.</li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\heat map of ppc report filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report heat map of ppc.png")

st.markdown("""<p class='text_left font_size_24' id="sale_comparison_report"><b>&#8658; Sale Comparison Report</b></p>
            <ul>
                <li>Select mode to group and unique data (Daily, Weekly, monthly, Quarter, and Yearly.</li>
                <li>Select status (Sale, New Arrival, Stock).</li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\sale comparison report filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report sale comparison.png")

st.markdown("""<p class='text_left font_size_24' id="tradescreen"><b>&#8658; Tradescreen</b></p>
            <ul>
                <li>Select Company (1, 2, 7, 9, Rap Net, Manufacturing).</li>
                <li>Select status (Sale, Stock).</li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\tradescreen filter.png")

st.markdown("""<p class="font_size_18">Report</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\report tradescreen.png")

st.markdown("""<p class='text_left font_size_24' id="stocksummary"><b>&#8658; Cno1 and Cno.2 Stock summary</b></p>
            <ul>
                <li>Select Mode (Disc% or PPC).</li>
                <li>Select Size Band (Rap Size, Pricing Size, Website Size).</li>
                <li>Select First Company (1, 2, 7, 9, Rap Net, Manufacturing).</li>
                <li>Select Report (Daily or Monthly).</li>
                <li>Select Range(1+ or Pointer).</li>
                <li>if Selected Report is Daily then.
                    <ul>
                        <li>Select Type (SALE or SATOCK).</li>
                        <li>Select Second Company (1, 2, 7, 9, Rap Net, Manufacturing).</li>
                    </ul>
                </li>
                <li>if Selected Report is Monthly then.
                    <ul>
                        <li>Select Start Date.</li>
                        <li>Select To Date.</li>
                    </ul>
                </li>
                <li>Click on View Report.</li>
            </ul>""", unsafe_allow_html=True)

st.markdown("""<p class="font_size_18">Daily Report Filter</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\Daily Cno1 and Cno.2 Stock summary.png")

st.markdown("""<p class="font_size_18">Daily eport</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\Daily Cno1 and Cno.2 Stock summary Report.png")

st.markdown("""<p class="font_size_18">Monthly Report Filter</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\Cno1 and Cno.2 Stock summary.png")

st.markdown("""<p class="font_size_18">Monthly eport</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\Monthly Cno1 and Cno.2 Stock summary Report.png")

st.markdown("""<p class="text_center bold_text font_size_28" id="cut_redefine">Cut Redefine Documentation</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\login.png")

st.markdown("<p class='text_left font_size_16'>First Select option name <b>Cut Redefine</b> in the select report button.</p>", unsafe_allow_html=True)
st.markdown("<p class='text_left font_size_16'>Then put a your user name and password</p>", unsafe_allow_html=True)
st.markdown("<p class='text_left font_size_16'>After that select a <b>stay login</b> checkbox. </p>", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\cur redefine home.png")
st.markdown("<p class='text_left font_size_16'>After select a <b>stay login</b> checkbox, there will be <b>sample file</b> button. Download it!</p>", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\sample file of cut redefine.png")
st.markdown("<p class='text_left font_size_16'>Your sample file look like this format. Now update your new data here and  save it.</p>", unsafe_allow_html=True)
st.markdown("<p class='text_left font_size_24'>NOTE : DON’T CHANGE FORMAT.</p>", unsafe_allow_html=True)
st.markdown("<p class='text_left font_size_16'>Now click on <b>browse files</b> button on website and select your sample file where you have updated your new data.</p>", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\final result of cut redefine.png")
st.markdown("<p class='text_left font_size_16'>After uploading, a dataframe will be displayed.</p>", unsafe_allow_html=True)
st.markdown("<p class='text_left font_size_16'>To download, click on <b>download excel file</b> button.</p>", unsafe_allow_html=True)

st.markdown("""<p class="text_center bold_text font_size_28" id="pricing">Pricing Documentation</p>""", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\login.png")

st.markdown("<p class='text_left font_size_16'>First Select option name <b>Pricing</b> in the select report button.</p>", unsafe_allow_html=True)
st.markdown("<p class='text_left font_size_16'>Then put a your user name and password</p>", unsafe_allow_html=True)
st.markdown("<p class='text_left font_size_16'>After that select a <b>stay login</b> checkbox. </p>", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\pricing home page.png")
st.markdown("<p class='text_left font_size_16'>After select a <b>stay login</b> checkbox, there will be <b>sample file</b> button. Download it!</p>", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\sample file of pricing.png")
st.markdown("<p class='text_left font_size_16'>Your sample file look like this format. Now update your new data here and  save it.</p>", unsafe_allow_html=True)
st.markdown("<p class='text_left font_size_24'>NOTE : DON’T CHANGE FORMAT.</p>", unsafe_allow_html=True)
st.markdown("<p class='text_left font_size_16'>Now click on <b>browse files</b> button on website and select your sample file where you have updated your new data.</p>", unsafe_allow_html=True)

show_img(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\image\output of pricing.png")
st.markdown("<p class='text_left font_size_16'>After uploading, a dataframe will be displayed.</p>", unsafe_allow_html=True)
st.markdown("<p class='text_left font_size_16'>To download, click on <b>download excel file</b> button.</p>", unsafe_allow_html=True)