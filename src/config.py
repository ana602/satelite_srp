from pathlib import Path

# Input file configuration
sat_file_id = "SUN190450"
station_file_id = "MGEX"
satelite_data_path = str(Path(__file__).parent.parent) + "\\input_data\\" + sat_file_id + ".txt"
mgex_path = str(Path(__file__).parent.parent) + "\\input_data\\" + station_file_id + ".txt"

# Output file configuration
satelites_b14_path = str(Path(__file__).parent.parent) + "\\gen_data\\" + sat_file_id + "_b14.txt"
satelites_2_path = str(Path(__file__).parent.parent) + "\\gen_data\\" + sat_file_id + "_2.txt"
satelites_angle_path = str(Path(__file__).parent.parent) + "\\gen_data\\" + sat_file_id + "_angle.txt"
satelites_angle2_path = str(Path(__file__).parent.parent) + "\\gen_data\\" + sat_file_id + "_angle2.txt"
satelites_stationsFiLa_path = str(Path(__file__).parent.parent) + "\\gen_data\\" + station_file_id + "_stationsFiLa.txt"
satelites_distance14_path = str(Path(__file__).parent.parent) + "\\gen_data\\" + sat_file_id + "_distance14.txt"