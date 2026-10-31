## **Disaster Recovery Management**

* This includes a set of procedures and plans used to:

  * Prevent disasters where possible

  * Minimise damage when disasters occur

  * Restore systems, data and business operations after a disaster

### Types of Disasters Causing Data Loss and Business Disruption

1. **Natural Disasters**

   * Fire

   * Floods

   * Earthquakes

   * Storms

   * Lightning strikes

   * **Effects**

     * Damage to buildings and equipment

     * Loss of access to systems

     * Data loss

2. **Equipment and power failures**

   * Hard disk failure

   * Server failure

   * Network device failure

   * Power cuts

   * Power surges

   * **Effects**

     * System downtime

     * Corrupted or lost data

     * Business interruption

3. **Cybercrime**

   * Hacking

   * DoS attacks

   * Data theft

   * Unauthorised access

   * **Effects**

     * Data breaches

     * Service disruption

     * Financial losses

4. **Malware**

   * Viruses

   * Worms

   * Trojans

   * Spyware

   * Ransomware

   * **Effects**

     * Data corruption

     * Data deletion

     * System failure

5. **Criminal Activity**

   * Theft of equipment

   * Sabotage

   * Insider attacks

   * **Effects**

     * Loss of hardware

     * Loss of confidential data

     * Business disruption

6. **Accidental Disruptive Events**

   * Accidental deletion of files

   * Misconfiguration of systems

   * Human error

   * Spilled liquids damaging equipment

   * **Effects**

     * Data loss

     * Downtime

     * Reduced productivity

### Risk Analysis

* This includes identification and evaluation of possible threats.

* The purpose is to determine the likelihood of a disaster occurring, the impact of the disaster if it occurs, and prioritising the risks.

* Qualitative risk analysis involves categorising the risks based on experience and expert judgement to rank them as high, medium, or low.

* Quantitative risk analysis involves consideration of loss of premises, loss of data, loss of IT systems, and loss of staff skills to measure the following:

  * Probability of occurrence: how likely it is for the risk to occur

  * Financial Cost: the cost of handling the damages

  * Severity of Consequence: measures how harsh, critical, or serious the outcome is

* Outcomes of risk analysis may include risk reports, risk priority lists, and disaster recovery plans.

### Perpetrator Analysis

* Identification of likely attackers and assessment of the threats that they pose.

* Possible attackers may include the following: Hackers, Crackers, Script kiddies, Terrorists, Business competitors, governments, and Malicious employees

* This analysis determines

  * Likelihood of attack

  * Type of attack

  * Resources required for protection

* This allows organisations to choose the appropriate

  * Firewalls

  * Anti-virus software

  * Anti-spyware software

  * Intrusion detection systems

* Advantages

  * Resources targeted at most likely threats

  * Better allocation of security budgets

  * Improved disaster recovery planning

### Risk Testing

* Checks whether the plans developed for disaster recovery work properly by testing them using different methods such as:

  * Simulated disaster scenarios

  * Computer modelling and simulations

  * Backup restoration tests

  * Security penetration testing

* The purpose includes

  * Identifying weaknesses in the plan

  * Verifying recovery procedures

  * Ensuring backups are usable

  * Confirming staff know procedures in case of a disaster

### Quantifying Risks

* Risks must be measured using:

  * The chance that they will occur. For instance, frequent power cuts have a high probability of occurring, whereas earthquakes have a low likelihood of occurring.

  * The consequences in case it occurs. E.g., temporary printer failures count as low impact, whereas loss of the customer database counts as a high-impact consequence.

* The risk level that is used to:

  * Prioritise threats

  * Allocate resources

  * Determine protection methods

### Control of Threats

1. **Anti-virus / Anti-malware Software**

   * Scans files and network traffic

   * Detects known malware signatures

   * Removes or quarantines threats

2. **Firewalls**

   * Monitor incoming and outgoing traffic

   * Block suspicious packets

   * Prevent unauthorised access

3. **Proxy Servers**

   * Filter incoming data

   * Can run anti-malware checks

4. **Monitoring and Logging**

   * First monitor

     * User activity

     * Login attempts

     * Network traffic

   * Then detect

     * Unusual behaviour

     * Suspicious access patterns

5. **Intrusion Detection Systems (IDS)**

   * Detect attacks

   * Generate alerts

   * May use honeypots/honey traps

* ### Restoring After a Disaster

  * Restoring backups

    * Files

    * Databases

    * Applications

    * Entire systems

  * Switch to Backup Systems

    * Secondary servers

    * Mirror systems

    * Disaster recovery sites

  * Reinstall Software

    * Operating systems

    * Applications

    * Security software

  * Resume Normal Operations

    * Verify data integrity

    * Test systems

    * Return services to users

### Strategies to Minimise Risks

* **Protection for Power Supplies**

  * Using surge protectors to protect equipment from voltage spikes and lightning-induced surges

  * UPS (uninterruptible power supply) provides temporary power during outages and time for safe shutdown

  * Backup generators to provide long-term emergency power. May be used for data centres and critical business operations

* **Password and access controls**

  * Password protection by using strong passwords and regularly changing them

  * Access Rights / Permissions to control who can

    * Read files

    * Modify files

    * Delete files

    * Execute programs

  * Advantages

    * Prevent unauthorised access

    * Protect confidential information

    * Reduce insider threats

* **Protection from Malware and Unauthorised Access**

  * Anti-virus software protects against viruses, worms and Trojans.

  * Anti-spyware software protects against spyware, keyloggers and data theft

  * Firewalls protect by filtering traffic and blocking attackers.

  * Physical security includes locked rooms, security guards, CCTV, and access cards

* **Backup Strategies**

  * The purpose of backups is to prevent loss of data from events such as
    * Data loss

    * Malware attacks

    * Hardware failures

    * Operating system failures
  * Types of Backups:
    1. **Tape-Based Backups**

       * Advantages

         * Very large storage capacity

         * Low cost per GB

         * Well-established technology

       * Disadvantages

         * Slow backup

         * Slow recovery

         * Fragile media

         * Compatibility issues

    2. **Hard Disk-Based Backups**

       * Advantages

         * Fast backup

         * Fast recovery

         * Direct access to files

         * Large capacities

       * Disadvantages

         * More expensive

         * Hard disk failure can cause data loss

    3. **Cloud-Based Backups**

       * Advantages

         * Off-site storage

         * Protection from local disasters

         * Maintenance handled by provider

         * Virtually unlimited capacity

       * Disadvantages

         * Requires reliable internet

         * Security concerns

         * Dependence on cloud provider
  * Technicians should perform regular backups daily, weekly or according to business requirements.
  * Automating backups ensures consistency and reduced human errors
  * Multiple copies of backups can be stored on different storage media or at different physical locations.
  * Storing backup copies away from work site allows protection against fire, flood and theft
  * Different backup types may include:
    * Full backup

    * Incremental backup

    * Differential backup
  * Maintaining backup records allows tracking of backup dates, storage locations, and recovery status.
  * Organisations must regularly test backups to confirm that they work correctly and that all data can be recovered in case of disaster

    #|
    ||
    
    Advantages

    |
    
    Disadvantages

    ||
    ||
    
    Quick recovery of lost data

    |
    
    Malware may be backed up

    ||
    ||
    
    Protection from malware damage

    |
    
    Data may not be fully up-to-date

    ||
    ||
    
    Protection from hardware failure

    |
    
    Storage costs

    ||
    ||
    
    Protection from power failures

    |
    
    Performance reduction during backup

    ||
    ||
    
    Protection from operating system failure

    |
    
    Restoration can be time-consuming

    ||
    ||
    
    ​

    |
    
    Backup media may be stolen if not encrypted

    ||
    |#
    
