-- ====================================================
-- View 1 : Beneficiary Summary
-- ====================================================

CREATE VIEW IF NOT EXISTS vw_beneficiaries_summary AS

SELECT

    territory,

    COUNT(DISTINCT beneficiary_uid) AS households_reached,

    SUM(hh_size) AS individuals_reached

FROM beneficiaries

GROUP BY territory;



-- ====================================================
-- View 2 : Distribution by Kit Type
-- ====================================================

CREATE VIEW IF NOT EXISTS vw_distribution_by_kit AS

SELECT

    item_kit_type,

    COUNT(*) AS distributions

FROM beneficiaries

GROUP BY item_kit_type;



-- ====================================================
-- View 3 : Enumerators Performance
-- ====================================================

CREATE VIEW IF NOT EXISTS vw_enumerator_performance AS

SELECT

    enumerator_id,

    COUNT(*) AS records_collected

FROM beneficiaries

GROUP BY enumerator_id;



-- ====================================================
-- View 4 : Daily Distribution
-- ====================================================

CREATE VIEW IF NOT EXISTS vw_daily_distribution AS

SELECT

    distribution_date,

    COUNT(*) AS households,

    SUM(hh_size) AS individuals

FROM beneficiaries

GROUP BY distribution_date;