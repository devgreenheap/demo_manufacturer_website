"""
Static content for GIO Electronics.

This module holds the site's product, service, industry and process data as
plain Python structures. It mirrors the shape of the MySQL-ready schema in
database/schema.sql, so swapping this for real database queries later is a
drop-in change (see database/schema.sql for the `products` table definition).
"""

CATEGORIES = [
    {
        "slug": "mobile-components",
        "name": "Mobile Components",
        "icon": "connector",
        "blurb": "Precision components for smartphones and handheld devices.",
    },
    {
        "slug": "computing-components",
        "name": "Computing Components",
        "icon": "usb",
        "blurb": "Connectors and internal components for laptops and computers.",
    },
    {
        "slug": "consumer-electronics",
        "name": "Consumer Electronics",
        "icon": "display",
        "blurb": "Components engineered for TVs and home entertainment systems.",
    },
    {
        "slug": "appliance-components",
        "name": "Appliance Components",
        "icon": "switch",
        "blurb": "Durable components built for home appliance manufacturing.",
    },
    {
        "slug": "electronic-components",
        "name": "Electronic Components",
        "icon": "chip",
        "blurb": "Core electronic components for general industrial use.",
    },
]

PRODUCTS = [
    # Mobile Components
    {
        "id": 1, "slug": "charging-connectors", "name": "Charging Connectors",
        "category": "Mobile Components", "category_slug": "mobile-components", "icon": "connector",
        "description": "High-durability charging connectors engineered for reliable power transfer in mobile devices.",
        "overview": "Our charging connectors are built for consistent contact performance across repeated insertion cycles, supporting fast-charging mobile device designs.",
        "applications": ["Smartphones", "Tablets", "Portable power banks", "Wearable charging docks"],
        "specifications": {"Contact Cycles": "10,000+ rated", "Current Rating": "Up to 5A", "Insertion Force": "Low to moderate"},
        "material": "Copper alloy contacts with gold-flash plating, high-temperature engineering plastic housing.",
        "dimensions": "Custom to device profile (standard and compact form factors available).",
        "compatibility": "USB-C, Micro-USB, and proprietary connector profiles on request.",
        "manufacturing_options": ["Prototype samples", "Low-volume pilot runs", "Full-scale production"],
        "quality_info": "Each batch undergoes contact-resistance testing and mechanical cycle testing before dispatch.",
    },
    {
        "id": 2, "slug": "speaker-modules", "name": "Speaker Modules",
        "category": "Mobile Components", "category_slug": "mobile-components", "icon": "speaker",
        "description": "Compact speaker modules tuned for clear audio output in space-constrained mobile enclosures.",
        "overview": "Designed for integration into slim mobile device housings without compromising acoustic performance.",
        "applications": ["Smartphones", "Tablets", "Portable media devices"],
        "specifications": {"Impedance": "8 ohm / 4 ohm options", "Frequency Response": "Custom tuned", "Mounting": "SMD / bracket mount"},
        "material": "Neodymium magnet, polymer diaphragm, ABS housing.",
        "dimensions": "Custom to enclosure cavity.",
        "compatibility": "Standard mobile PCB mounting profiles.",
        "manufacturing_options": ["Custom acoustic tuning", "Prototype samples", "Bulk production"],
        "quality_info": "Acoustic output and frequency response are verified on sample units from every production batch.",
    },
    {
        "id": 3, "slug": "microphones", "name": "Microphones",
        "category": "Mobile Components", "category_slug": "mobile-components", "icon": "mic",
        "description": "Miniature microphone components for clear voice capture in mobile and wearable devices.",
        "overview": "Engineered for consistent sensitivity and noise performance in compact device designs.",
        "applications": ["Smartphones", "Headsets", "Wearables", "Voice-enabled devices"],
        "specifications": {"Sensitivity": "Custom to application", "Type": "MEMS / electret options", "Mounting": "SMD"},
        "material": "MEMS silicon element or electret capsule with protective housing.",
        "dimensions": "Miniature SMD package sizes.",
        "compatibility": "Standard mobile and wearable PCB layouts.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Sensitivity and noise-floor checks are performed as part of production quality control.",
    },
    {
        "id": 4, "slug": "flex-cables", "name": "Flex Cables",
        "category": "Mobile Components", "category_slug": "mobile-components", "icon": "cable",
        "description": "Flexible printed circuit cables for reliable internal connections in compact devices.",
        "overview": "Built to withstand repeated flexing while maintaining stable electrical connections inside mobile assemblies.",
        "applications": ["Smartphones", "Tablets", "Foldable devices", "Compact electronics"],
        "specifications": {"Layers": "Single / double / multi-layer", "Flex Cycles": "Rated per design", "Connector": "ZIF / board-to-board"},
        "material": "Polyimide base film with copper conductive traces.",
        "dimensions": "Custom to internal routing path.",
        "compatibility": "ZIF connectors and board-to-board interfaces.",
        "manufacturing_options": ["Custom trace design", "Prototype samples", "Bulk production"],
        "quality_info": "Flex-cycle durability and continuity are tested prior to shipment.",
    },
    {
        "id": 5, "slug": "buttons-switches", "name": "Buttons & Switches",
        "category": "Mobile Components", "category_slug": "mobile-components", "icon": "switch",
        "description": "Tactile buttons and switches designed for consistent feel and long operational life.",
        "overview": "Provide reliable tactile feedback across power, volume, and function controls on mobile devices.",
        "applications": ["Smartphones", "Tablets", "Remote controls", "Handheld devices"],
        "specifications": {"Life Cycle": "100,000+ actuations rated", "Actuation Force": "Custom tuned", "Type": "Tactile dome / mechanical"},
        "material": "Stainless steel contacts, engineering plastic housing.",
        "dimensions": "Custom to device control layout.",
        "compatibility": "Standard mobile device control assemblies.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Actuation force and cycle life are verified through mechanical testing.",
    },
    # Computing Components
    {
        "id": 6, "slug": "laptop-connectors", "name": "Laptop Connectors",
        "category": "Computing Components", "category_slug": "computing-components", "icon": "connector",
        "description": "Robust connectors engineered for internal and external laptop interfaces.",
        "overview": "Built to handle frequent connect/disconnect cycles common in laptop use while maintaining stable signal integrity.",
        "applications": ["Laptops", "Notebooks", "Docking stations"],
        "specifications": {"Contact Cycles": "10,000+ rated", "Signal Type": "Power / data", "Mounting": "Board mount"},
        "material": "Copper alloy contacts, high-temperature plastic housing.",
        "dimensions": "Custom to chassis design.",
        "compatibility": "Standard laptop motherboard and chassis interfaces.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Contact resistance and durability are verified before dispatch.",
    },
    {
        "id": 7, "slug": "usb-ports", "name": "USB Ports",
        "category": "Computing Components", "category_slug": "computing-components", "icon": "usb",
        "description": "USB port components built for reliable data and power connectivity in computing devices.",
        "overview": "Designed to standard USB specifications with attention to durability under repeated use.",
        "applications": ["Laptops", "Desktops", "Peripherals", "Docking hardware"],
        "specifications": {"Type": "USB-A / USB-C options", "Current Rating": "Per USB spec", "Mounting": "SMD / through-hole"},
        "material": "Copper alloy contacts, engineering plastic shell, metal shielding.",
        "dimensions": "Standard USB footprint.",
        "compatibility": "USB-A, USB-C interfaces.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Signal integrity and mechanical durability are tested per batch.",
    },
    {
        "id": 8, "slug": "power-connectors-computing", "name": "Power Connectors",
        "category": "Computing Components", "category_slug": "computing-components", "icon": "power",
        "description": "Power delivery connectors designed for stable performance in computing hardware.",
        "overview": "Engineered to maintain consistent power delivery under varying load conditions in computing systems.",
        "applications": ["Laptops", "Desktops", "Power adapters"],
        "specifications": {"Current Rating": "Custom to application", "Voltage Rating": "Custom to application", "Mounting": "Board / panel mount"},
        "material": "Copper alloy contacts, flame-retardant plastic housing.",
        "dimensions": "Custom to power supply design.",
        "compatibility": "Standard computing power interfaces.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Load and thermal performance are checked during production.",
    },
    {
        "id": 9, "slug": "internal-cables", "name": "Internal Cables",
        "category": "Computing Components", "category_slug": "computing-components", "icon": "cable",
        "description": "Internal wiring and cable assemblies for computing hardware.",
        "overview": "Custom cable assemblies that route power and data reliably within computing chassis designs.",
        "applications": ["Desktops", "Laptops", "Servers", "Peripheral hardware"],
        "specifications": {"Conductor Type": "Stranded copper", "Insulation": "PVC / TPE options", "Connector": "Custom to application"},
        "material": "Stranded copper conductors with insulated jacket.",
        "dimensions": "Custom length and gauge.",
        "compatibility": "Custom to chassis routing requirements.",
        "manufacturing_options": ["Custom cable assembly design", "Prototype samples", "Bulk production"],
        "quality_info": "Continuity and insulation testing performed on every batch.",
    },
    {
        "id": 10, "slug": "cooling-components", "name": "Cooling Components",
        "category": "Computing Components", "category_slug": "computing-components", "icon": "chip",
        "description": "Thermal management components supporting stable operation of computing hardware.",
        "overview": "Designed to support efficient heat dissipation in compact and high-performance computing systems.",
        "applications": ["Laptops", "Desktops", "Servers"],
        "specifications": {"Type": "Fan components / heat spreaders", "Mounting": "Chassis-specific", "Airflow": "Custom to design"},
        "material": "Aluminum / copper thermal elements, engineering plastic housings.",
        "dimensions": "Custom to chassis thermal design.",
        "compatibility": "Standard computing chassis mounting points.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Thermal and mechanical performance verified before shipment.",
    },
    # Consumer Electronics
    {
        "id": 11, "slug": "tv-components", "name": "TV Components",
        "category": "Consumer Electronics", "category_slug": "consumer-electronics", "icon": "display",
        "description": "Internal components engineered for television manufacturing and assembly.",
        "overview": "Support reliable operation of display, control, and power subsystems within television assemblies.",
        "applications": ["Televisions", "Home entertainment systems"],
        "specifications": {"Type": "Custom to subsystem", "Mounting": "Board / chassis mount", "Rating": "Custom to application"},
        "material": "Custom per component subtype.",
        "dimensions": "Custom to chassis design.",
        "compatibility": "Standard television chassis architectures.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Components are inspected and tested according to subsystem requirements.",
    },
    {
        "id": 12, "slug": "display-connectors", "name": "Display Connectors",
        "category": "Consumer Electronics", "category_slug": "consumer-electronics", "icon": "connector",
        "description": "Connectors engineered for stable signal transfer to display panels.",
        "overview": "Maintain consistent signal integrity between control boards and display panels in consumer electronics.",
        "applications": ["Televisions", "Monitors", "Display panels"],
        "specifications": {"Signal Type": "LVDS / FPC interfaces", "Pitch": "Custom to panel spec", "Mounting": "Board mount"},
        "material": "Copper alloy contacts, engineered plastic housing.",
        "dimensions": "Custom to panel interface.",
        "compatibility": "Standard display panel connector profiles.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Signal continuity is verified on every production batch.",
    },
    {
        "id": 13, "slug": "power-components-consumer", "name": "Power Components",
        "category": "Consumer Electronics", "category_slug": "consumer-electronics", "icon": "power",
        "description": "Power supply components for consumer electronics manufacturing.",
        "overview": "Support stable and efficient power delivery within consumer electronics product designs.",
        "applications": ["Televisions", "Audio systems", "Consumer appliances"],
        "specifications": {"Voltage Rating": "Custom to application", "Current Rating": "Custom to application", "Mounting": "Board / panel mount"},
        "material": "Copper alloy contacts, flame-retardant housing materials.",
        "dimensions": "Custom to product design.",
        "compatibility": "Standard consumer electronics power interfaces.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Electrical and thermal performance are checked before dispatch.",
    },
    {
        "id": 14, "slug": "control-components", "name": "Control Components",
        "category": "Consumer Electronics", "category_slug": "consumer-electronics", "icon": "switch",
        "description": "Control interface components for consumer electronics devices.",
        "overview": "Provide reliable user-control interfaces integrated into consumer electronics product designs.",
        "applications": ["Televisions", "Remote controls", "Home entertainment systems"],
        "specifications": {"Type": "Buttons / rotary / touch interfaces", "Life Cycle": "Custom rated", "Mounting": "Board / panel mount"},
        "material": "Engineering plastic and metal contact elements.",
        "dimensions": "Custom to product control layout.",
        "compatibility": "Standard consumer electronics control assemblies.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Actuation and durability testing performed during production.",
    },
    # Appliance Components
    {
        "id": 15, "slug": "washing-machine-components", "name": "Washing Machine Components",
        "category": "Appliance Components", "category_slug": "appliance-components", "icon": "chip",
        "description": "Electronic components engineered for washing machine control and operation.",
        "overview": "Built to withstand the operating conditions of home appliance environments while maintaining reliable performance.",
        "applications": ["Washing machines", "Laundry appliances"],
        "specifications": {"Type": "Control / sensor components", "Rating": "Appliance-grade", "Mounting": "Custom to chassis"},
        "material": "Moisture-resistant housings with corrosion-resistant contacts.",
        "dimensions": "Custom to appliance chassis design.",
        "compatibility": "Standard washing machine control architectures.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Components are tested for durability under appliance operating conditions.",
    },
    {
        "id": 16, "slug": "control-switches-appliance", "name": "Control Switches",
        "category": "Appliance Components", "category_slug": "appliance-components", "icon": "switch",
        "description": "Durable control switches engineered for home appliance interfaces.",
        "overview": "Provide dependable switching performance for appliance control panels under everyday use.",
        "applications": ["Home appliances", "Kitchen equipment", "Laundry appliances"],
        "specifications": {"Life Cycle": "Appliance-grade rated", "Actuation Force": "Custom tuned", "Type": "Rocker / push / rotary"},
        "material": "Stainless steel contacts, heat-resistant plastic housing.",
        "dimensions": "Custom to appliance panel layout.",
        "compatibility": "Standard home appliance control panels.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Switching life and contact reliability are verified before dispatch.",
    },
    {
        "id": 17, "slug": "wiring-components", "name": "Wiring Components",
        "category": "Appliance Components", "category_slug": "appliance-components", "icon": "cable",
        "description": "Internal wiring harnesses and components for appliance manufacturing.",
        "overview": "Custom wiring assemblies designed to route power and control signals reliably within appliance housings.",
        "applications": ["Home appliances", "Kitchen equipment", "Laundry appliances"],
        "specifications": {"Conductor Type": "Stranded copper", "Insulation": "Heat-resistant jacket", "Connector": "Custom to application"},
        "material": "Stranded copper conductors with heat-resistant insulation.",
        "dimensions": "Custom length and gauge.",
        "compatibility": "Custom to appliance chassis routing.",
        "manufacturing_options": ["Custom harness design", "Prototype samples", "Bulk production"],
        "quality_info": "Continuity and insulation integrity are tested on every batch.",
    },
    {
        "id": 18, "slug": "connectors-appliance", "name": "Connectors",
        "category": "Appliance Components", "category_slug": "appliance-components", "icon": "connector",
        "description": "General-purpose connectors engineered for appliance assembly.",
        "overview": "Support reliable electrical connections between subsystems within home appliance assemblies.",
        "applications": ["Home appliances", "Kitchen equipment"],
        "specifications": {"Current Rating": "Custom to application", "Mounting": "Board / wire-to-wire", "Contact Cycles": "Appliance-grade rated"},
        "material": "Copper alloy contacts, heat-resistant plastic housing.",
        "dimensions": "Custom to appliance design.",
        "compatibility": "Standard appliance interconnect profiles.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Contact resistance and mechanical durability are verified before dispatch.",
    },
    # Electronic Components
    {
        "id": 19, "slug": "connectors-general", "name": "Connectors",
        "category": "Electronic Components", "category_slug": "electronic-components", "icon": "connector",
        "description": "General-purpose electronic connectors for a wide range of industrial applications.",
        "overview": "Versatile connector solutions engineered to customer specifications across multiple industries.",
        "applications": ["Industrial equipment", "Electronic assemblies", "Custom devices"],
        "specifications": {"Current Rating": "Custom to application", "Mounting": "Board / panel / wire-to-wire", "Contact Cycles": "Custom rated"},
        "material": "Copper alloy contacts, engineering plastic housing.",
        "dimensions": "Custom to application.",
        "compatibility": "Custom to customer specification.",
        "manufacturing_options": ["Custom design", "Prototype samples", "Bulk production"],
        "quality_info": "Electrical and mechanical performance verified before dispatch.",
    },
    {
        "id": 20, "slug": "terminals", "name": "Terminals",
        "category": "Electronic Components", "category_slug": "electronic-components", "icon": "chip",
        "description": "Precision terminals for secure electrical connections in industrial assemblies.",
        "overview": "Manufactured to maintain secure, low-resistance connections across a range of electronic assemblies.",
        "applications": ["Industrial equipment", "Control panels", "Electronic assemblies"],
        "specifications": {"Type": "Ring / spade / blade terminals", "Current Rating": "Custom to application", "Material Finish": "Tin / gold plating options"},
        "material": "Copper alloy with plated finish.",
        "dimensions": "Custom to wire gauge and application.",
        "compatibility": "Standard wire gauges and terminal blocks.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Crimp integrity and contact resistance are tested per batch.",
    },
    {
        "id": 21, "slug": "switches-general", "name": "Switches",
        "category": "Electronic Components", "category_slug": "electronic-components", "icon": "switch",
        "description": "Industrial-grade switches for general electronic and control applications.",
        "overview": "Engineered for dependable switching performance across industrial and consumer applications.",
        "applications": ["Industrial equipment", "Control panels", "Consumer devices"],
        "specifications": {"Type": "Toggle / push / rocker", "Life Cycle": "Custom rated", "Current Rating": "Custom to application"},
        "material": "Stainless steel contacts, engineering plastic housing.",
        "dimensions": "Custom to application.",
        "compatibility": "Standard panel-mount and board-mount profiles.",
        "manufacturing_options": ["Prototype samples", "Bulk production"],
        "quality_info": "Switching life and contact reliability are verified before dispatch.",
    },
    {
        "id": 22, "slug": "sensors", "name": "Sensors",
        "category": "Electronic Components", "category_slug": "electronic-components", "icon": "chip",
        "description": "Sensor components engineered for accurate detection in industrial and consumer applications.",
        "overview": "Support precise monitoring and control functions across a variety of electronic systems.",
        "applications": ["Industrial equipment", "Home appliances", "Consumer electronics", "IoT devices"],
        "specifications": {"Type": "Custom to application", "Output": "Analog / digital", "Mounting": "Board / panel mount"},
        "material": "Custom per sensor type.",
        "dimensions": "Custom to application.",
        "compatibility": "Custom to customer control system.",
        "manufacturing_options": ["Custom calibration", "Prototype samples", "Bulk production"],
        "quality_info": "Accuracy and repeatability are verified during production testing.",
    },
    {
        "id": 23, "slug": "custom-components", "name": "Custom Components",
        "category": "Electronic Components", "category_slug": "electronic-components", "icon": "chip",
        "description": "Fully custom electronic components engineered to customer specification.",
        "overview": "Our engineering team works with customers to design and manufacture components tailored to specific requirements.",
        "applications": ["Custom industrial equipment", "Specialized electronic assemblies"],
        "specifications": {"Type": "Customer-defined", "Rating": "Customer-defined", "Mounting": "Customer-defined"},
        "material": "Selected based on application requirements.",
        "dimensions": "Fully customized to specification.",
        "compatibility": "Designed to customer system requirements.",
        "manufacturing_options": ["Custom design & engineering", "Prototype development", "Bulk production"],
        "quality_info": "Custom components follow a dedicated inspection and testing plan agreed with the customer.",
    },
]

SERVICES = [
    {
        "icon": "manufacture", "name": "Custom Component Manufacturing",
        "description": "Manufacturing electronic components according to customer requirements and specifications.",
    },
    {
        "icon": "pcb", "name": "PCB Assembly",
        "description": "Professional assembly and testing of electronic components on printed circuit boards.",
    },
    {
        "icon": "assembly", "name": "Electronic Product Assembly",
        "description": "Assembly of electronic parts and sub-components.",
    },
    {
        "icon": "prototype", "name": "Prototype Development",
        "description": "Development of prototypes before mass production.",
    },
    {
        "icon": "test", "name": "Component Testing & Quality Inspection",
        "description": "Testing components for performance, reliability, consistency, and quality.",
    },
    {
        "icon": "contract", "name": "Contract Manufacturing",
        "description": "Manufacturing electronic products and components according to customer requirements.",
    },
    {
        "icon": "design", "name": "Custom Design & Engineering",
        "description": "Technical support and customized engineering solutions.",
    },
    {
        "icon": "package", "name": "Packaging & Labelling",
        "description": "Professional packaging, identification, labelling, and bulk-order preparation.",
    },
]

INDUSTRIES = [
    {"icon": "mobile", "name": "Mobile & Smart Devices"},
    {"icon": "usb", "name": "Computers & IT Hardware"},
    {"icon": "display", "name": "Consumer Electronics"},
    {"icon": "switch", "name": "Home Appliances"},
    {"icon": "chip", "name": "Industrial Electronics"},
    {"icon": "connector", "name": "Automotive Electronics"},
    {"icon": "signal", "name": "Telecommunications"},
    {"icon": "iot", "name": "IoT & Connected Devices"},
]

PROCESS_STEPS = [
    {"name": "Requirement", "description": "Understanding customer specifications, application needs, and technical requirements."},
    {"name": "Design & Engineering", "description": "Engineering the component or assembly design to meet functional and manufacturing requirements."},
    {"name": "Prototype", "description": "Developing prototype samples for validation before production begins."},
    {"name": "Manufacturing", "description": "Producing components at prototype, pilot, or full production scale."},
    {"name": "Testing & Quality Control", "description": "Verifying performance, reliability, and consistency against specifications."},
    {"name": "Packaging", "description": "Preparing components for safe transport with proper identification and labelling."},
    {"name": "Delivery", "description": "Delivering finished components and assemblies to the customer."},
]

QUALITY_POINTS = [
    {"icon": "material", "name": "Material Inspection", "description": "Incoming materials are checked against specification before entering production."},
    {"icon": "production", "name": "Production Quality Checks", "description": "In-process checks are carried out at key stages of manufacturing."},
    {"icon": "test", "name": "Component Testing", "description": "Components are tested for electrical and mechanical performance."},
    {"icon": "performance", "name": "Performance Testing", "description": "Functional testing verifies components perform as intended under expected conditions."},
    {"icon": "final", "name": "Final Inspection", "description": "A final review is carried out before components are approved for dispatch."},
    {"icon": "package", "name": "Packaging Inspection", "description": "Packaging is checked to ensure components are protected during transport."},
]

QUALITY_TRUST_CARDS = [
    {"name": "Precision", "description": "Attention to technical detail throughout the manufacturing process."},
    {"name": "Reliability", "description": "Components built to perform consistently in real-world use."},
    {"name": "Consistency", "description": "Repeatable quality across every production batch."},
    {"name": "Quality Control", "description": "Structured inspection at every stage of manufacturing."},
]

WHY_GIO = [
    {"icon": "precision", "name": "Precision Manufacturing", "description": "Components produced with attention to technical requirements and consistency."},
    {"icon": "quality", "name": "Quality Focus", "description": "Structured inspection and testing throughout manufacturing."},
    {"icon": "custom", "name": "Custom Solutions", "description": "Solutions tailored to specific business requirements."},
    {"icon": "support", "name": "Reliable Support", "description": "Technical assistance from requirement to production."},
    {"icon": "scale", "name": "Scalable Manufacturing", "description": "Solutions for prototype and larger production requirements."},
    {"icon": "b2b", "name": "B2B Expertise", "description": "Focused on serving businesses and industrial customers."},
]

TRUST_INDICATORS = [
    {"icon": "precision", "name": "Precision Manufacturing"},
    {"icon": "quality", "name": "Quality Focus"},
    {"icon": "custom", "name": "Custom Solutions"},
    {"icon": "b2b", "name": "B2B Manufacturing"},
]

COMPANY_INFO = {
    "name": "GIO Electronics",
    "tagline": "Engineering Components for a Connected World.",
    "phone": "+91 XXXXX XXXXX",  # placeholder
    "email": "info@gioelectronics.com",  # placeholder
    "address": "Chennai, Tamil Nadu, India",  # placeholder
}


CATEGORY_ILLUSTRATIONS = {
    "mobile-components": "mobile",
    "computing-components": "computing",
    "consumer-electronics": "consumer",
    "appliance-components": "appliance",
    "electronic-components": "electronic",
}

for _p in PRODUCTS:
    _p["illustration"] = CATEGORY_ILLUSTRATIONS[_p["category_slug"]]
for _c in CATEGORIES:
    _c["illustration"] = CATEGORY_ILLUSTRATIONS[_c["slug"]]


def get_product_by_slug(slug):
    return next((p for p in PRODUCTS if p["slug"] == slug), None)


def get_related_products(product, limit=3):
    related = [p for p in PRODUCTS if p["category"] == product["category"] and p["id"] != product["id"]]
    return related[:limit]


def get_products_by_category(category_slug):
    return [p for p in PRODUCTS if p["category_slug"] == category_slug]
