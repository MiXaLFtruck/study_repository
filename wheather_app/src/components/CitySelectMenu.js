import React from "react";
import { cities } from "../constants";

function CitySelectMenu(props) {
	return (
		<div className={props.menuActive ? "popup-menu open" : "popup-menu"} onClick={ () => { props.setMenuActive(false); } }>
			<div className="city-menu">
				<div className="list-group">
					{cities.map((city) => <button key={city.name} type="button" className="list-group-item list-group-item-action"
					onClick={() => {
						props.setCurrentCity(city);
						props.newResponse();
						}}>
							{city.name}, {city.countryCode}
						</button>)
					}
				</div>
			</div>
		</div>
	);
}

export default CitySelectMenu;
