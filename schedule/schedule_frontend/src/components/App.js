import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
            loaded: false,
            placeholder: "Loading"
        };
    }

    componentDidMount() {
        fetch("api/schedules")
            .then(response => {
                if (response.status > 400) {
                    return this.setState(() => {
                        return { placeholder: "Something went wrong!" };
                    });
                }
                return response.json();
            })
            .then(data => {
                this.setState(() => {
                    return {
                        data,
                        loaded: true
                    };
                });
            });
    }

    render() {
        return (
            <section>
                {this.state.data.map(schedules => {
                    return (
                        <div class="card">
                            <div class="card-header">
                                {schedules.schedule_date} - {schedules.schedule_time}
                            </div>
                            <div class="card-body">
                                <h5 class="card-title">{schedules.title}</h5>
                                <p class="card-text">{schedules.schedule_date} - {schedules.schedule_time}</p>
                                <p class="card-text">Dr. {schedules.doctor_name} - {schedules.doctor_expertise}</p>
                            </div>
                        </div>
                    );
                })}
            </section >
        );
    }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);