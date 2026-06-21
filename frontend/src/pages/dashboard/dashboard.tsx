import "../../style/main/section.css";
import "../../style/elements/card.css";
import "../../style/elements/chart.css";
import { StatCard1, StatCard2, StatCard3 } from "./stat_card";
import { ChartAreaStep } from "./chart"

const chartData = [
    { month: "January", data: 9 },
    { month: "February", data: 204 },
    { month: "March", data: 180 },
    { month: "April", data: 120 },
    { month: "May", data: 180 },
    { month: "June", data: 42 },
];

const DashBoard = () => {
    return (
        <main>
            <section className="section">
                <div className="section__inner">
                    <div className="section__header section__left">
                        <p className="section__eyebrow">// air quality and climate change</p>
                        <p className="section__title">OVERVIEW</p>
                        <div className="section__header">Overview</div>
                    </div>
                    <div className="section__left bento__grid">
                        <StatCard1 label="PM2.5" unit="μg/m³" />
                        <StatCard2 label="PM10" unit="μg/m³" />
                        <StatCard3 label="AQI Status" />
                        <StatCard1 label="Climate Trend" />
                    </div>
                </div>
            </section>
            <section className="section section--dark">
                <div className="section__header">
                    <p className="section__title" style={{ color: "var(--surface)" }}> AIR QUALITY</p>
                </div>
                <div className="bento-card bento-card--safety">
                    <div className="bento-card__number">over time</div>
                    <div className="section__header">
                        <p className="section__title">PM2.5</p>
                        <div className="bento-card__nonshadow">
                            <ChartAreaStep chartData={chartData} />
                        </div>
                    </div>
                    <div>
                        <div className="section__title">PM10</div>
                        <div className="bento-card__nonshadow">
                            <ChartAreaStep chartData={chartData} />
                        </div>
                    </div>
                </div>
            </section>
        </main>
    )
};

export { DashBoard };