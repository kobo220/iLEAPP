__artifacts_v2__ = {
    "applelocationd": {
        "name": "Location Services",
        "description": "Extracts location services settings",
        "author": "@AlexisBrignoni",
        "version": "0.2.3",
        "date": "2023-10-03",
        "requirements": "none",
        "category": "Identifiers",
        "notes": "",
        "paths": ('*/mobile/Library/Preferences/com.apple.locationd.plist'),
        "output_types": ["html", "tsv", "lava"]
    }
}

import plistlib
from scripts.ilapfuncs import artifact_processor, device_info, webkit_timestampsconv

@artifact_processor
def applelocationd(files_found, report_folder, seeker, wrap_text, timezone_offset):
    data_list = []
    source_path = str(files_found[0])

    with open(source_path, "rb") as fp:
        pl = plistlib.load(fp)
        for key, val in pl.items():
            if key == 'LocationServicesEnabledIn8.0':
                data_list.append(('Location Services Enabled', val))
                device_info("Settings", "Location Services Enabled", val, source_path)
            
            elif key == 'LastSystemVersion':
                data_list.append(('Last System Version', val))
                device_info("Settings", "Last System Version", val, source_path)
                
            elif key == 'steadinessClassificationNextClassificationTime' or key == 'VO2MaxCloudKitLastForcedFetch' \
                or key == 'kP6MWDNextEstimateTime' or key == 'VO2MaxCloudKitManagerNextActivityTime':
                val = webkit_timestampsconv(val)
                data_list.append((key, val))
            else:
                data_list.append((key, val))
                
    data_headers = ('Property', 'Property Value')     
    return data_headers, data_list, source_path
